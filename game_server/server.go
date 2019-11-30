package main

//TO DO: ADD CHECK TO SEE IF THE CLIENT IS STILL IN THE QUEUE
import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"net"
	. "sudo-ku/board/handler"
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

func readPacket(conn net.Conn) (packet, error) {
	var p packet
	payload := make([]byte, 200)
	r := bufio.NewReader(conn)

	t, err := r.ReadByte()
	if err != nil {
		fmt.Println("tcp connection error:", err)
		conn.Close()
		return p, err
	}

	size, err := r.ReadByte()
	if err != nil {
		fmt.Println("tcp connection error:", err)
		conn.Close()
		return p, err
	}

	_, err = io.ReadFull(r, payload[:int(size)])
	if err != nil {
		fmt.Println("tcp connection error:", err)
		conn.Close()
		return p, err
	}

	return packet{Type: t, Size: size, Payload: payload[:int(size)]}, nil
}

func writePacket(conn net.Conn, p packet) error {
	data := append([]byte{p.Type}, []byte{p.Size}...)
	data = append(data, p.Payload...)
	_, err := conn.Write(data)
	return err
}
func handleMatchInit(conn net.Conn, matchChannel chan matchRequestMsg) {

	p, err := readPacket(conn)
	if err != nil {
		return
	}
	//At this point we're going to check the token for authentication,
	//if it's valid the client connection is going to be forwarded to
	//the match server, along with the chosen difficulty level and
	//the user name
	var decodedReq clientMatchRequestMsg
	json.Unmarshal(p.Payload, &decodedReq)

	fmt.Println(decodedReq)
	valid, err := utils.VerifyToken(decodedReq.Token)
	if valid && (err == nil) {
		payload, err := utils.DecodeToken(decodedReq.Token)
		if err != nil {
			return
		}
		netData, err := json.Marshal(clientMatchResponseMsg{Status: 0})
		//TO DO: ADD CHECK
		err = writePacket(conn, MakePacket(matchRequestAckPkt, netData))
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

func handleConnectionIn(c net.Conn, ch chan<- packet) {
	for {
		p, err := readPacket(c)
		if err != nil {
			fmt.Println("", err)
			c.Close()
			return
		}
		ch <- p
	}
}

func handleConnectionOut(c net.Conn, ch <-chan packet) {
	for {
		p := <-ch
		err := writePacket(c, p)
		if err != nil {
			fmt.Println("", err)
		}
	}
}

func gameServerChallenge(c1 matchRequestMsg, c2 matchRequestMsg) {
	ch1In := make(chan packet)
	ch1Out := make(chan packet)
	ch2In := make(chan packet)
	ch2Out := make(chan packet)

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
	var sudokuBoard1 SudokuBoard
	json.Unmarshal(sudokuBoard1JSON, &sudokuBoard1)
	sudokuBoard2 := sudokuBoard1

	startMatchMsg1, err1 := json.Marshal(matchFoundMsg{OpponentUsername: c2.username, Board: sudokuBoard1.GetBoard()})
	startMatchMsg2, err2 := json.Marshal(matchFoundMsg{OpponentUsername: c1.username, Board: sudokuBoard1.GetBoard()})

	if err1 != nil || err2 != nil {
		fmt.Println("ops")
		ch1Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
		ch2Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
	}

	ch1Out <- MakePacket(matchFoundPkt, startMatchMsg1)
	ch2Out <- MakePacket(matchFoundPkt, startMatchMsg2)

	var moveDecoded moveMsg
	for {
		select {
		case p1 := <-ch1In:
			{
				switch p1.Type {
				case movePkt:
					json.Unmarshal([]byte(p1.Payload), &moveDecoded)

					r, done1, err := handleMoveMsgChallenge(&sudokuBoard1, moveDecoded)
					if err != nil {
						ch1Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
						ch2Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
						c1.conn.Close()
						c2.conn.Close()
						return
					}
					ch1Out <- MakePacket(moveOutcomePkt, r)
					if done1 {
						ch2Out <- MakePacket(opponentDonePkt, []byte{})
					}
				}
			}

		case p2 := <-ch2In:
			{
				json.Unmarshal([]byte(p2.Payload), &moveDecoded)
				switch p2.Type {
				case movePkt:
					r, done2, err := handleMoveMsgChallenge(&sudokuBoard2, moveDecoded)
					if err != nil {
						ch1Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
						ch2Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
						c1.conn.Close()
						c2.conn.Close()
						return
					}
					ch2Out <- MakePacket(moveOutcomePkt, r)
					if done2 {
						ch1Out <- MakePacket(opponentDonePkt, []byte{})
					}
				}
			}
		}
	}
}

func gameServerCollaborative(c1 matchRequestMsg, c2 matchRequestMsg) {
	ch1In := make(chan packet)
	ch1Out := make(chan packet)
	ch2In := make(chan packet)
	ch2Out := make(chan packet)

	go handleConnectionIn(c1.conn, ch1In)
	go handleConnectionOut(c1.conn, ch1Out)
	go handleConnectionIn(c2.conn, ch2In)
	go handleConnectionOut(c2.conn, ch2Out)

	//var sudokuBoard1 handler.SudokuBoard = handler.SudokuBoard(generator.MakeSudokuBoard(c1.difficulty))
	sudokuBoardg := model.SudokuBoard{
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
	sudokuBoardJSON, _ := json.Marshal(sudokuBoardg)
	var sudokuBoard SudokuBoard
	json.Unmarshal(sudokuBoardJSON, &sudokuBoard)

	startMatchMsg1, err1 := json.Marshal(matchFoundMsg{OpponentUsername: c2.username, Board: sudokuBoard.GetBoard()})
	startMatchMsg2, err2 := json.Marshal(matchFoundMsg{OpponentUsername: c1.username, Board: sudokuBoard.GetBoard()})

	if err1 != nil || err2 != nil {
		fmt.Println("ops")
		ch1Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
		ch2Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
	}

	ch1Out <- MakePacket(matchFoundPkt, startMatchMsg1)
	ch2Out <- MakePacket(matchFoundPkt, startMatchMsg2)

	var moveDecoded moveMsg

	for {
		select {
		case p1 := <-ch1In:
			{
				switch p1.Type {
				case movePkt:
					json.Unmarshal([]byte(p1.Payload), &moveDecoded)

					r, r2, _, err := handleMoveMsgCollaborative(&sudokuBoard, moveDecoded)
					if err != nil {
						ch1Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
						ch2Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
						c1.conn.Close()
						c2.conn.Close()
						return
					}
					ch1Out <- MakePacket(moveOutcomePkt, r)
					if r2 != nil {
						ch2Out <- MakePacket(changeValuePkt, r2)
					}
				}
			}

		case p2 := <-ch2In:
			{
				json.Unmarshal([]byte(p2.Payload), &moveDecoded)
				switch p2.Type {
				case movePkt:
					r, r2, _, err := handleMoveMsgCollaborative(&sudokuBoard, moveDecoded)
					if err != nil {
						ch1Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
						ch2Out <- MakePacket(errorPkt, []byte(`{msg":"internal server error"}`))
						c1.conn.Close()
						c2.conn.Close()
						return
					}
					ch2Out <- MakePacket(moveOutcomePkt, r)
					if r2 != nil {
						ch1Out <- MakePacket(changeValuePkt, r2)
					}
				}
			}
		}
	}
}

func handleMoveMsgChallenge(s *SudokuBoard, m moveMsg) (r []byte, done bool, err error) {
	done = false
	legal, remaining := (*s).Move(m.Row, m.Col, m.Value)

	if remaining == 0 {
		done = true
	}

	r, err = json.Marshal(moveOutcomeMsg{IsLegal: legal, Done: done})
	return
}

func handleMoveMsgCollaborative(s *SudokuBoard, m moveMsg) (r, r2 []byte, done bool, err error) {
	done = false
	legal, remaining := (*s).Move(m.Row, m.Col, m.Value)

	if remaining == 0 {
		done = true
	}

	if legal {
		r2, _ = json.Marshal(changeValueMsg{m.Row, m.Col, m.Value, done})
	}
	r, err = json.Marshal(moveOutcomeMsg{IsLegal: legal, Done: done})
	return
}
