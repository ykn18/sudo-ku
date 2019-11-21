package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net"
)

//This struct represents the request forwarded to the match server after
//the initial check
type matchRequest struct {
	conn       net.Conn
	difficulty string
	mode       int
}

type clientMatchRequest struct {
	Token      string `json:"token"`
	Difficulty string `json:"difficulty"`
	Mode       int    `json:"mode"`
}

var difficulties = [...]string{"easy", "medium", "hard"}

func main() {
	matchChannel := make(chan matchRequest)
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

func handleMatchInit(conn net.Conn, matchChannel chan matchRequest) {
	jsonData, err := bufio.NewReader(conn).ReadString('\n')
	//The following line is going to be modified once the separator has been agreed
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
	var decodedReq clientMatchRequest
	json.Unmarshal([]byte(jsonData), &decodedReq)

	//TO DO: some check on the token and then:
	matchChannel <- matchRequest{conn: conn, difficulty: decodedReq.Difficulty, mode: decodedReq.Mode}
}

func matchServer(matchChannel chan matchRequest) {
	//Players are matched solely based on the chosen difficulty level and mode

	//Creates a map containing the references to the queues for the collaborative
	//mode and another map containing the references to the queus for the challenge mode
	matchingQueuesChallenge := map[string]*[]matchRequest{}
	matchingQueuesCollaborative := map[string]*[]matchRequest{}
	var queues *map[string]*[]matchRequest

	//Initializes the queues for the difficulty levels specified before
	for _, v := range difficulties {
		matchingQueuesChallenge[v] = &[]matchRequest{}
		matchingQueuesCollaborative[v] = &[]matchRequest{}
	}

	for {
		currentRequest := <-matchChannel
		fmt.Println(currentRequest.difficulty)
		fmt.Println(currentRequest.mode)
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
			go gameServer(r.conn, currentRequest.conn)
		} else {
			*m = append(*m, currentRequest)
		}
	}
}

func handleConnectionIn(c net.Conn, ch chan<- string) {
	for {
		netData, err := bufio.NewReader(c).ReadString('\n')

		if err != nil {
			fmt.Println("", err)
			c.Close()
			return
		}
		ch <- netData
	}
}

func handleConnectionOut(c net.Conn, ch <-chan string) {
	for {
		netData := <-ch
		fmt.Println(netData)

		size, err := c.Write([]byte(netData))
		if err != nil {
			fmt.Println("", err)
		}
		_ = size
	}
}

func gameServer(c1 net.Conn, c2 net.Conn) {

	ch1In := make(chan string)
	ch1Out := make(chan string)

	go handleConnectionIn(c1, ch1In)
	go handleConnectionOut(c1, ch1Out)

	ch2In := make(chan string)
	ch2Out := make(chan string)

	go handleConnectionIn(c2, ch2In)
	go handleConnectionOut(c2, ch2Out)

	for {
		select {
		case msg1 := <-ch1In:
			ch2Out <- msg1
		case msg2 := <-ch2In:
			ch1Out <- msg2
		}
	}
}
