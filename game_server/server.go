package main

//TO DO: ADD CHECK TO SEE IF THE CLIENT IS STILL IN THE QUEUE
import (
	"bufio"
	"encoding/json"
	"fmt"
	"net"
	"sudo-ku/board/handler"
	"sudo-ku/board/model"
	"sudo-ku/game_server/utils"
)

var difficulties = [...]string{"easy", "medium", "hard"}

func main() {
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

func handleMatchInit(conn net.Conn, matchChannel chan matchRequestMsg) {
	jsonData, err := bufio.NewReader(conn).ReadString('|')
	jsonData = jsonData[:len(jsonData)-1]

	if err != nil {
		fmt.Println("tcp connection error:", err)
		conn.Close()
		return
	}
	//At this point we're going to check the token for authentication,
	//if it's valid the client connection is going to be forwarded to
	//the match server, along with the chosen difficulty level and
	//the user name
	var decodedReq clientMatchRequestMsg
	json.Unmarshal([]byte(jsonData), &decodedReq)

	valid, err := utils.VerifyToken(decodedReq.Token)
	if valid && (err == nil) {
		payload, err := utils.DecodeToken(decodedReq.Token)
		if err != nil {
			return
		}
		netData, err := json.Marshal(clientMatchResponseMsg{Status: 0})
		//TO DO: ADD CHECK
		_, err = conn.Write([]byte(netData))
		if err != nil {
			fmt.Println("", err)
		}
		matchChannel <- matchRequestMsg{conn: conn, difficulty: decodedReq.Difficulty, mode: decodedReq.Mode, username: payload.Username}
	}
	//TO DO: return error
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
			//TO DO: return an error to the client for the chosen mode and close the connection
			continue
		}
		m, ok := (*queues)[currentRequest.difficulty]

		//Check if the difficulty of the last request extracted from the channel is legal
		if !ok {
			//TO DO: return an error to the client for the chosen difficulty and close the connection
		}
		if len(*m) > 0 {
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

func handleConnectionIn(c net.Conn, ch chan<- []byte) {
	for {
		netData, err := bufio.NewReader(c).ReadSlice(byte('|'))
		if err != nil {
			fmt.Println("", err)
			c.Close()
			return
		}
		netData = netData[:len(netData)-1]
		ch <- netData
	}
}

func handleConnectionOut(c net.Conn, ch <-chan []byte) {
	for {
		netData := <-ch
		size, err := c.Write(append(netData, []byte("|")...))
		if err != nil {
			fmt.Println("", err)
		}
		_ = size
	}
}

func gameServerChallenge(c1 matchRequestMsg, c2 matchRequestMsg) {
	fmt.Println("matchsgtaring")
	ch1In := make(chan []byte)
	ch1Out := make(chan []byte)
	ch2In := make(chan []byte)
	ch2Out := make(chan []byte)

	go handleConnectionIn(c1.conn, ch1In)
	go handleConnectionOut(c1.conn, ch1Out)
	go handleConnectionIn(c2.conn, ch2In)
	go handleConnectionOut(c2.conn, ch2Out)

	//var sudokuBoard1 handler.SudokuBoard = handler.SudokuBoard(generator.MakeSudokuBoard(c1.difficulty))
	sudokuBoard1g := model.SudokuBoard{
		Board: [9][9]int{{5, 0, 3, 4, 7, 1, 2, 6, 0},
			{4, 0, 0, 0, 5, 0, 0, 0, 0},
			{9, 0, 0, 0, 6, 0, 5, 0, 0},
			{0, 0, 0, 0, 3, 0, 0, 0, 2},
			{1, 0, 5, 0, 0, 0, 0, 0, 0},
			{6, 0, 9, 1, 8, 0, 0, 5, 0},
			{0, 0, 0, 0, 2, 0, 0, 8, 3},
			{3, 4, 6, 0, 9, 0, 0, 0, 0},
			{0, 0, 8, 7, 0, 0, 6, 0, 5}},
		Solution: [9][9]int{{5, 8, 3, 4, 7, 1, 2, 6, 9},
			{4, 6, 7, 2, 5, 9, 3, 1, 8},
			{9, 1, 2, 3, 6, 8, 5, 7, 4},
			{8, 7, 4, 5, 3, 6, 1, 9, 2},
			{1, 2, 5, 9, 4, 7, 8, 3, 6},
			{6, 3, 9, 1, 8, 2, 4, 5, 7},
			{7, 5, 1, 6, 2, 4, 9, 8, 3},
			{3, 4, 6, 8, 9, 5, 7, 2, 1},
			{2, 9, 8, 7, 1, 3, 6, 4, 5}},
		Blanks: 49,
	}
	sudokuBoard1JSON, _ := json.Marshal(sudokuBoard1g)
	var sudokuBoard1 handler.SudokuBoard
	json.Unmarshal(sudokuBoard1JSON, &sudokuBoard1)
	sudokuBoard2 := sudokuBoard1
	startMatchMsg1, err1 := json.Marshal(matchFoundMsg{OpponentUsername: c2.username, Board: sudokuBoard1.GetBoard()})
	startMatchMsg2, err2 := json.Marshal(matchFoundMsg{OpponentUsername: c1.username, Board: sudokuBoard1.GetBoard()})

	if err1 != nil || err2 != nil {
		fmt.Println("ops")
		return //TO DO: ADD SOMETHING
	}

	ch1Out <- startMatchMsg1
	ch2Out <- startMatchMsg2
	var decodedMsg moveMsg
	done := false

	for {
		select {
		case msg1 := <-ch1In:
			{
				json.Unmarshal([]byte(msg1), &decodedMsg)
				fmt.Println(decodedMsg)
				legal, remaining := sudokuBoard1.Move(decodedMsg.Row, decodedMsg.Col, decodedMsg.Value)

				if remaining == 0 {
					done = true
					msg, _ := json.Marshal(doneMsg{Type: "done", OpponentDone: sudokuBoard1.CheckSolution()})
					ch2Out <- msg
				}
				ans, err := json.Marshal(moveOutcomeMsg{IsLegal: legal, Done: done})
				if err != nil {
					ch1Out <- []byte(`{"type":"error", "msg":"internal server error"}`)
					ch2Out <- []byte(`{"type":"error", "msg":"internal server error"}`)
					c1.conn.Close()
					c2.conn.Close()
					return
				}
				ch1Out <- ans
			}

		case msg2 := <-ch2In:
			{
				json.Unmarshal([]byte(msg2), &decodedMsg)
				legal, remaining := sudokuBoard2.Move(decodedMsg.Row, decodedMsg.Col, decodedMsg.Value)
				if remaining == 0 {
					done = true
					msg, _ := json.Marshal(doneMsg{Type: "done", OpponentDone: sudokuBoard2.CheckSolution()})
					ch1Out <- msg
				}
				ans, err := json.Marshal(moveOutcomeMsg{IsLegal: legal, Done: done})
				if err != nil {
					ch1Out <- []byte(`{"type":"error", "msg":"internal server error"}`)
					ch2Out <- []byte(`{"type":"error", "msg":"internal server error"}`)
					c1.conn.Close()
					c2.conn.Close()
					return
				}
				ch2Out <- ans
			}
		}
	}
}

func gameServerCollaborative(c1 matchRequestMsg, c2 matchRequestMsg) {
}
