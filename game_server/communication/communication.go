package communication

import (
	"bufio"
	"fmt"
	"io"
	"net"
)

const (
	MatchRequestPkt  byte = 1
	MatchFoundPkt    byte = 2
	CheckSolutionPkt byte = 3
	ValidSolutionPkt byte = 4
	DonePkt          byte = 5
	MovePkt          byte = 6
	ChangeValuePkt   byte = 7
	PingPkt          byte = 8
	PingAckPkt       byte = 9
	ErrorPkt         byte = 10
)

type Packet struct {
	Type    byte
	Size    byte
	Payload []byte
}

func MakePacket(t byte, payload []byte) Packet {
	var p Packet
	p.Type = t
	p.Size = byte(len(payload))
	p.Payload = payload
	return p
}

func IsOpen(conn net.Conn) bool {
	err := WritePacket(conn, MakePacket(PingPkt, []byte{}))
	if err != nil {
		return false
	}
	p, err := ReadPacket(conn)
	if p.Type == PingAckPkt && err == nil {
		return true
	}
	return false
}

func ReadPacket(conn net.Conn) (Packet, error) {
	var p Packet
	payload := make([]byte, 200)
	r := bufio.NewReader(conn)

	t, err := r.ReadByte()
	if err != nil {
		return p, err
	}

	size, err := r.ReadByte()
	if err != nil {
		return p, err
	}

	if size == 0 {
		return Packet{Type: t, Size: size, Payload: []byte{}}, nil
	}
	_, err = io.ReadFull(r, payload[:int(size)])
	if err != nil {
		return p, err
	}

	p = Packet{Type: t, Size: size, Payload: payload[:int(size)]}
	fmt.Println("I received:", string(p.Type), string(p.Size), string(p.Payload))
	return p, nil
}

func WritePacket(conn net.Conn, p Packet) error {
	fmt.Println("I'm sending:", string(p.Type), string(p.Size), string(p.Payload))
	data := append([]byte{p.Type}, []byte{p.Size}...)
	if p.Size > 0 {
		data = append(data, p.Payload...)
	}

	_, err := conn.Write(data)
	return err
}

type ClientMatchRequestMsg struct {
	Token      string `json:"token"`
	Difficulty string `json:"difficulty"`
	Mode       int    `json:"mode"`
}
type ClientMatchResponseMsg struct {
	Status int `json:"status"`
}

type MatchFoundMsg struct {
	OpponentUsername string    `json:"opponentUsername"`
	Board            [9][9]int `json:"board"`
}

type MoveMsg struct {
	Row   int `json:"row"`
	Col   int `json:"col"`
	Value int `json:"value"`
}

type MoveOutcomeMsg struct {
	IsLegal bool `json:"isLegal"`
}

type ChangeValueMsg struct {
	Row   int  `json:"row"`
	Col   int  `json:"col"`
	Value int  `json:"value"`
	Done  bool `json:"done"`
}

type ErrorMsg struct {
	Msg string `json:"msg"`
}

type CheckSolutionMsg struct {
	Board [9][9]int `json:"board"`
}

type DoneMsg struct {
	Done bool `json:"done"`
}

type ValidSolutionMsg struct {
	Valid bool `json:"valid"`
}
