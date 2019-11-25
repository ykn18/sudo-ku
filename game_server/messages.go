package main

import "net"

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
	Type  string `json:"type"`
	Row   int    `json:"row"`
	Col   int    `json:"col"`
	Value int    `json:"value"`
}

type moveOutcomeMsg struct {
	Type    string `json:"type"`
	IsLegal bool   `json:"isLegal"`
	Done    bool   `json:"done"`
}

type doneMsg struct {
	Type         string `json:"type"`
	OpponentDone bool   `json:"opponentDone"`
}

type changeValueMsg struct {
	Type  string `json:"type"`
	Row   int    `json:"row"`
	Col   int    `json:"col"`
	Value int    `json:"value"`
	Done  bool   `json:"done"`
}

type errorMsg struct {
	Type string `json:"type"`
	Msg  string `json:"msg"`
}
