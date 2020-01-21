package main

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"os"
	"time"

	. "github.com/ykn18/sudo-ku/board/handler"
	"github.com/ykn18/sudo-ku/board/model"
	. "github.com/ykn18/sudo-ku/game_server/communication"
	"github.com/ykn18/sudo-ku/utils"
)

type matchRequestMsg struct {
	conn       net.Conn
	difficulty string
	mode       int
	username   string
}

type serverAuthReq struct {
	Servername string `json:"servername"`
	Password   string `json:"password"`
}

type serverAuthRes struct {
	Token string `json:"token"`
}

type MatchResult struct {
	Win       bool      `json:"win,omitempty"`
	MatchTime int       `json:"matchTime,omitempty"`
	DateTime  time.Time `json:"dateTime,omitempty"`
}

const userSecretKey = "usersecretkey"

var errBadRequest = errors.New("Bad request")
var errInternal = errors.New("Internal server error")

var difficulties = [...]string{"easy", "medium", "hard"}

var token = ""
var full bool

func main() {
	/*
		full = flag.Bool("full", false, "If full is set an almost full sudoku board is going to be used")
		flag.Parse()
	*/
	if os.Getenv("FULL") == "true" {
		full = true
	}

	for token == "" {
		token = getServerToken()
		time.Sleep(500 * time.Millisecond)
	}

	matchChannel := make(chan matchRequestMsg)
	go matchServer(matchChannel)

	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		fmt.Println("tcp server listener error:", err)
	}

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("tcp server listener error:", err)
		}

		go handleMatchInit(conn, matchChannel)
	}
}

func getServerToken() string {
	authURI := "http://authserver:5000/servers/auth"
	requestBody, err := json.Marshal(serverAuthReq{
		Servername: "gameserver",
		Password:   "gameserver",
	})

	if err != nil {
		return ""
	}

	resp, err := http.Post(authURI, "application/json", bytes.NewBuffer(requestBody))
	if err != nil {
		fmt.Println(err)
		return ""
	}

	defer resp.Body.Close()
	bodyJSON, err := ioutil.ReadAll(resp.Body)
	var body serverAuthRes
	json.Unmarshal(bodyJSON, &body)
	return body.Token
}
func handleMatchInit(conn net.Conn, matchChannel chan matchRequestMsg) {

	p, err := ReadPacket(conn)
	if err != nil {
		return
	}
	//At this point we're going to check the token for authentication,
	//if it's valid the client connection is going to be forwarded to
	//the match server, along with the chosen difficulty level and
	//the user name
	var decodedReq ClientMatchRequestMsg
	json.Unmarshal(p.Payload, &decodedReq)

	valid, err := utils.VerifyToken(decodedReq.Token, userSecretKey)
	if valid && (err == nil) {
		payload, err := utils.DecodeToken(decodedReq.Token)
		if err != nil {
			return
		}
		matchChannel <- matchRequestMsg{conn: conn, difficulty: decodedReq.Difficulty, mode: decodedReq.Mode, username: payload.Username}
	} else {
		WritePacket(conn, MakePacket(ErrorPkt, []byte(`{"msg":"Authentication error"}`)))
	}
}

func matchServer(matchChannel chan matchRequestMsg) {
	//Players are matched solely based on the chosen difficulty level and mode

	//Creates a map containing the references to the queues for the collaborative
	//mode and another map containing the references to the queus for the challenge mode
	matchingQueuesChallenge := map[string]*[]matchRequestMsg{}
	matchingQueuesCollaborative := map[string]*[]matchRequestMsg{}
	var queues *map[string]*[]matchRequestMsg

	//Initializes the queues for the difficulty levels specified before
	for _, v := range difficulties {
		matchingQueuesChallenge[v] = &[]matchRequestMsg{}
		matchingQueuesCollaborative[v] = &[]matchRequestMsg{}
	}

	for {
		currentRequest := <-matchChannel
		//Check if the mode of the last request extracted from the channel is legal
		if currentRequest.mode == 0 {
			queues = &matchingQueuesChallenge
		} else if currentRequest.mode == 1 {
			queues = &matchingQueuesCollaborative
		} else {
			WritePacket(currentRequest.conn, MakePacket(ErrorPkt, []byte(`{"msg":"Bad request"}`)))
			continue
		}
		m, ok := (*queues)[currentRequest.difficulty]

		//Check if the difficulty of the last request extracted from the channel is legal
		if !ok {
			WritePacket(currentRequest.conn, MakePacket(ErrorPkt, []byte(`{"m"sg":"Bad request"}`)))
			continue
		}

		for len(*m) > 0 && !IsOpen((*m)[0].conn) {
			*m = (*m)[1:]
			fmt.Println("Removing closed connection")
			fmt.Println(*m)
		}

		if len(*m) > 0 {
			if (*m)[0].username == currentRequest.username {
				WritePacket(currentRequest.conn, MakePacket(ErrorPkt, []byte(`{"msg":"Are you trying to play with yourself?"}`)))
				continue
			}
			r := (*m)[0]
			*m = (*m)[1:]
			//Passes the connections of the matched players to the goroutine that manages
			//the game session
			if currentRequest.mode == 0 {
				go gameServerChallenge(r, currentRequest)
			} else {
				go gameServerCollaborative(r, currentRequest)
			}
		} else {
			*m = append(*m, currentRequest)
		}
	}
}

func handleConnectionIn(c net.Conn, ch chan<- Packet) {
	for {
		p, err := ReadPacket(c)
		if err != nil {
			fmt.Println("Closing the reader socket")
			c.Close()
			//A reader goroutine sending an empty packet means that it is closing the connection
			//because the client is down or the match has finished and is returning
			ch <- Packet{}
			return
		}
		ch <- p
	}
}

func handleConnectionOut(c net.Conn, ch <-chan Packet) {
	for {
		p := <-ch
		//A writer goroutine receiving an empty packet has to close the connection and return
		if p.Type == 0 {
			fmt.Println("Closing the writer socket")
			c.Close()
			return
		}
		err := WritePacket(c, p)
		if err != nil {
			c.Close()
			return
		}
	}
}

func gameServerChallenge(c1 matchRequestMsg, c2 matchRequestMsg) {
	ch1In := make(chan Packet)
	ch1Out := make(chan Packet)
	ch2In := make(chan Packet)
	ch2Out := make(chan Packet)

	go handleConnectionIn(c1.conn, ch1In)
	go handleConnectionOut(c1.conn, ch1Out)
	go handleConnectionIn(c2.conn, ch2In)
	go handleConnectionOut(c2.conn, ch2Out)

	var sudokuBoard1 SudokuBoard

	if !full {
		url := "http://generator:7070/board/difficulty=" + c1.difficulty
		client := &http.Client{}
		req, _ := http.NewRequest("GET", url, nil)
		req.Header.Set("Authorization", "Bearer "+token)
		res, _ := client.Do(req)
		body, _ := ioutil.ReadAll(res.Body)

		json.Unmarshal(body, &sudokuBoard1)
	} else {
		sudokuBoard1g := model.SudokuBoard{
			Board: [9][9]int{
				{5, 8, 3, 4, 7, 1, 2, 6, 9},
				{4, 6, 7, 2, 5, 9, 0, 0, 8},
				{9, 1, 2, 3, 6, 8, 0, 0, 4},
				{8, 7, 0, 5, 3, 6, 1, 9, 2},
				{1, 2, 5, 9, 4, 7, 8, 3, 6},
				{6, 3, 9, 1, 8, 2, 4, 5, 7},
				{7, 0, 1, 6, 2, 0, 9, 8, 3},
				{3, 4, 6, 8, 9, 5, 7, 2, 1},
				{2, 9, 8, 7, 1, 3, 6, 4, 5}},
			Solution: [9][9]int{
				{5, 8, 3, 4, 7, 1, 2, 6, 9},
				{4, 6, 7, 2, 5, 9, 3, 1, 8},
				{9, 1, 2, 3, 6, 8, 5, 7, 4},
				{8, 7, 4, 5, 3, 6, 1, 9, 2},
				{1, 2, 5, 9, 4, 7, 8, 3, 6},
				{6, 3, 9, 1, 8, 2, 4, 5, 7},
				{7, 5, 1, 6, 2, 4, 9, 8, 3},
				{3, 4, 6, 8, 9, 5, 7, 2, 1},
				{2, 9, 8, 7, 1, 3, 6, 4, 5}},
		}
		sudokuBoard1JSON, _ := json.Marshal(sudokuBoard1g)
		json.Unmarshal(sudokuBoard1JSON, &sudokuBoard1)
	}

	sudokuBoard2 := sudokuBoard1

	startMatchMsg1, err1 := json.Marshal(MatchFoundMsg{OpponentUsername: c2.username, Board: sudokuBoard1.GetBoard()})
	startMatchMsg2, err2 := json.Marshal(MatchFoundMsg{OpponentUsername: c1.username, Board: sudokuBoard1.GetBoard()})

	if err1 != nil || err2 != nil {
		fmt.Println("ops")
		ch1Out <- MakePacket(ErrorPkt, []byte(`{"msg":"internal server error"}`))
		ch2Out <- MakePacket(ErrorPkt, []byte(`{"msg":"internal server error"}`))
	}

	ch1Out <- MakePacket(MatchFoundPkt, startMatchMsg1)
	ch2Out <- MakePacket(MatchFoundPkt, startMatchMsg2)
	startTime := time.Now()

	var solutionDecoded CheckSolutionMsg

	for {
		select {
		case p1 := <-ch1In:
			{
				switch p1.Type {
				case 0:
					ch2Out <- MakePacket(ErrorPkt, []byte(`{"msg":"Opponent left, you win!"}`))
					ch1Out <- Packet{}
					ch2Out <- Packet{}
					sendStats(c1.username, c2.username, true, false, int(time.Now().Sub(startTime).Seconds()))
					return
				case CheckSolutionPkt:
					json.Unmarshal([]byte(p1.Payload), &solutionDecoded)
					v := sudokuBoard1.CheckSolution(solutionDecoded.Board)
					r, _ := json.Marshal(ValidSolutionMsg{Valid: v})
					ch1Out <- MakePacket(ValidSolutionPkt, r)
					if v {
						msg, _ := json.Marshal(DoneMsg{Done: true})
						ch2Out <- MakePacket(DonePkt, msg)
						sendStats(c1.username, c2.username, true, false, int(time.Now().Sub(startTime).Seconds()))
						ch1Out <- Packet{}
						ch2Out <- Packet{}
						return
					}
				}
			}

		case p2 := <-ch2In:
			{
				switch p2.Type {
				case 0:
					ch1Out <- MakePacket(ErrorPkt, []byte(`{"msg":"Opponent left, you win!"}`))
					sendStats(c1.username, c2.username, false, true, int(time.Now().Sub(startTime).Seconds()))
					ch1Out <- Packet{}
					ch2Out <- Packet{}
					return
				case CheckSolutionPkt:
					json.Unmarshal([]byte(p2.Payload), &solutionDecoded)
					v := sudokuBoard2.CheckSolution(solutionDecoded.Board)
					r, _ := json.Marshal(ValidSolutionMsg{Valid: v})
					ch2Out <- MakePacket(ValidSolutionPkt, r)
					if v {
						msg, _ := json.Marshal(DoneMsg{Done: true})
						ch1Out <- MakePacket(DonePkt, msg)
						sendStats(c1.username, c2.username, false, true, int(time.Now().Sub(startTime).Seconds()))
						ch1Out <- Packet{}
						ch2Out <- Packet{}
						return
					}
				}
			}
		}
	}
}

func gameServerCollaborative(c1 matchRequestMsg, c2 matchRequestMsg) {
	ch1In := make(chan Packet)
	ch1Out := make(chan Packet)
	ch2In := make(chan Packet)
	ch2Out := make(chan Packet)

	go handleConnectionIn(c1.conn, ch1In)
	go handleConnectionOut(c1.conn, ch1Out)
	go handleConnectionIn(c2.conn, ch2In)
	go handleConnectionOut(c2.conn, ch2Out)

	var sudokuBoard SudokuBoard
	if !full {
		url := "http://generator:7070/board/difficulty=" + c1.difficulty
		client := &http.Client{}
		req, _ := http.NewRequest("GET", url, nil)
		req.Header.Set("Authorization", "Bearer "+token)
		res, _ := client.Do(req)
		body, _ := ioutil.ReadAll(res.Body)

		json.Unmarshal(body, &sudokuBoard)
	} else {
		sudokuBoard1g := model.SudokuBoard{
			Board: [9][9]int{
				{5, 8, 3, 4, 7, 1, 2, 6, 9},
				{4, 6, 7, 2, 5, 9, 0, 0, 8},
				{9, 1, 2, 3, 6, 8, 0, 0, 4},
				{8, 7, 0, 5, 3, 6, 1, 9, 2},
				{1, 2, 5, 9, 4, 7, 8, 3, 6},
				{6, 3, 9, 1, 8, 2, 4, 5, 7},
				{7, 0, 1, 6, 2, 0, 9, 8, 3},
				{3, 4, 6, 8, 9, 5, 7, 2, 1},
				{2, 9, 8, 7, 1, 3, 6, 4, 5}},
			Solution: [9][9]int{
				{5, 8, 3, 4, 7, 1, 2, 6, 9},
				{4, 6, 7, 2, 5, 9, 3, 1, 8},
				{9, 1, 2, 3, 6, 8, 5, 7, 4},
				{8, 7, 4, 5, 3, 6, 1, 9, 2},
				{1, 2, 5, 9, 4, 7, 8, 3, 6},
				{6, 3, 9, 1, 8, 2, 4, 5, 7},
				{7, 5, 1, 6, 2, 4, 9, 8, 3},
				{3, 4, 6, 8, 9, 5, 7, 2, 1},
				{2, 9, 8, 7, 1, 3, 6, 4, 5}},
		}
		sudokuBoard1JSON, _ := json.Marshal(sudokuBoard1g)
		json.Unmarshal(sudokuBoard1JSON, &sudokuBoard)
	}

	startMatchMsg1, err1 := json.Marshal(MatchFoundMsg{OpponentUsername: c2.username, Board: sudokuBoard.GetBoard()})
	startMatchMsg2, err2 := json.Marshal(MatchFoundMsg{OpponentUsername: c1.username, Board: sudokuBoard.GetBoard()})

	if err1 != nil || err2 != nil {
		fmt.Println("ops")
		ch1Out <- MakePacket(ErrorPkt, []byte(`{"msg":"internal server error"}`))
		ch2Out <- MakePacket(ErrorPkt, []byte(`{"msg":"internal server error"}`))
	}

	ch1Out <- MakePacket(MatchFoundPkt, startMatchMsg1)
	ch2Out <- MakePacket(MatchFoundPkt, startMatchMsg2)

	startTime := time.Now()
	doneMsg, _ := json.Marshal(DoneMsg{Done: true})

	for {
		select {
		case p1 := <-ch1In:
			{
				switch p1.Type {
				case 0:
					ch2Out <- MakePacket(ErrorPkt, []byte(`{"msg":"Your friend left, game over!"}`))
					sendStats(c1.username, c2.username, false, false, int(time.Now().Sub(startTime).Seconds()))
					ch1Out <- Packet{}
					ch2Out <- Packet{}
					return
				case MovePkt:
					r, done, err := handleMoveMsgCollaborative(&sudokuBoard, p1)
					if err != nil {
						if err == errBadRequest {
							fmt.Println(err)
							continue
						} else {
							fmt.Println(err)
							ch1Out <- Packet{}
							ch2Out <- Packet{}
							return
						}
					}
					ch2Out <- MakePacket(ChangeValuePkt, r)
					if done {
						ch1Out <- MakePacket(DonePkt, doneMsg)
						ch2Out <- MakePacket(DonePkt, doneMsg)
						sendStats(c1.username, c2.username, true, true, int(time.Now().Sub(startTime).Seconds()))
						ch1Out <- Packet{}
						ch2Out <- Packet{}
						return
					}
				}
			}

		case p2 := <-ch2In:
			{
				switch p2.Type {
				case 0:
					ch1Out <- MakePacket(ErrorPkt, []byte(`{"msg":"Your friend left, game over!"}`))
					sendStats(c1.username, c2.username, false, false, int(time.Now().Sub(startTime).Seconds()))
					ch1Out <- Packet{}
					ch2Out <- Packet{}
					return
				case MovePkt:
					r, done, err := handleMoveMsgCollaborative(&sudokuBoard, p2)
					if err != nil {
						if err == errBadRequest {
							fmt.Println(err)
							continue
						} else {
							fmt.Println(err)
							ch1Out <- Packet{}
							ch2Out <- Packet{}
							return
						}
					}
					ch1Out <- MakePacket(ChangeValuePkt, r)
					if done {
						ch1Out <- MakePacket(DonePkt, doneMsg)
						ch2Out <- MakePacket(DonePkt, doneMsg)
						sendStats(c1.username, c2.username, true, true, int(time.Now().Sub(startTime).Seconds()))
						ch1Out <- Packet{}
						ch2Out <- Packet{}
						return
					}
				}
			}
		}
	}
}

func handleMoveMsgCollaborative(s *SudokuBoard, p Packet) (r []byte, done bool, err error) {
	var moveDecoded MoveMsg

	err = json.Unmarshal([]byte(p.Payload), &moveDecoded)

	if err != nil {
		err = errBadRequest
		return
	}

	allowed, remaining := (*s).Move(moveDecoded.Row, moveDecoded.Col, moveDecoded.Value)

	if !allowed {
		err = errBadRequest
		return
	}

	changeValResponse, err := json.Marshal(ChangeValueMsg{Row: moveDecoded.Row, Col: moveDecoded.Col, Value: moveDecoded.Value})

	if err != nil {
		err = errInternal
		return
	}
	r = changeValResponse
	if remaining == 0 && (*s).CheckSolution((*s).GetBoard()) {
		done = true
	}
	return r, done, err
}

func sendStats(user1, user2 string, win1, win2 bool, matchTime int) {
	client := &http.Client{}

	statsURI := "http://statisticserver:5050/user/" + user1 + "/result"
	requestBody, _ := json.Marshal(MatchResult{
		Win:       win1,
		MatchTime: matchTime,
		DateTime:  time.Now(),
	})
	req, _ := http.NewRequest("POST", statsURI, bytes.NewBuffer(requestBody))
	req.Header.Set("Authorization", "Bearer "+token)
	req.Header.Set("Content-Type", "application/json")
	res, _ := client.Do(req)
	fmt.Println(res.Status)

	statsURI = "http://statisticserver:5050/user/" + user2 + "/result"
	requestBody, _ = json.Marshal(MatchResult{
		Win:       win2,
		MatchTime: matchTime,
		DateTime:  time.Now(),
	})
	req, _ = http.NewRequest("POST", statsURI, bytes.NewBuffer(requestBody))
	req.Header.Set("Authorization", "Bearer "+token)
	req.Header.Set("Content-Type", "application/json")
	res, _ = client.Do(req)
	fmt.Println(res.Status)
}
