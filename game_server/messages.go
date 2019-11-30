package main

import "net"

const (
	matchRequestPkt    byte = 0
	matchRequestAckPkt byte = 1
	matchFoundPkt      byte = 2
	movePkt            byte = 3
	moveOutcomePkt     byte = 4
	opponentDonePkt    byte = 5
	changeValuePkt     byte = 6
	errorPkt           byte = 7
)

//Not an actual msg between client and server
type packet struct {
	Type    byte
	Size    byte
	Payload []byte
}

func MakePacket(t byte, payload []byte) packet {
	var p packet
	size := len(payload)
	p.Type = t
	p.Size = byte(size)
	p.Payload = payload
	return p
}

type matchRequestMsg struct {
	conn       net.Conn
	difficulty string
	mode       int
	username   string
}

type clientMatchRequestMsg struct {
	Token      string `json:"token"`
	Difficulty string `json:"difficulty"`
	Mode       int    `json:"mode"`
}
type clientMatchResponseMsg struct {
	Status int `json:"status"`
}

type matchFoundMsg struct {
	OpponentUsername string    `json:"opponentUsername"`
	Board            [9][9]int `json:"board"`
}

type moveMsg struct {
	Row   int `json:"row"`
	Col   int `json:"col"`
	Value int `json:"value"`
}

type moveOutcomeMsg struct {
	IsLegal bool `json:"isLegal"`
	Done    bool `json:"done"`
}

type opponentDoneMsg struct {
	OpponentDone bool `json:"opponentDone"`
}

type changeValueMsg struct {
	Row   int  `json:"row"`
	Col   int  `json:"col"`
	Value int  `json:"value"`
	Done  bool `json:"done"`
}

type errorMsg struct {
	Msg string `json:"msg"`
}
