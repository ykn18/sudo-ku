package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sudo-ku/board/generator"
	"sudo-ku/board/handler"
)

func main() {
	//ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
	//client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://localhost:27017"))
	/*
		r := mux.NewRouter()

		r.HandleFunc("/board", getBoard)

		http.ListenAndServe(":8080", r)
	*/

	/*
	var s generator.SudokuBoard
	var c int
	c = 0
	s = generator.MakeSudokuBoard("easy")
	for _, vi := range s.Board {
		for _, vj := range vi {
			if vj != 0 {
				c++
			}
		}
	}*/
	s := generator.MakeSudokuBoard("easy")
	fmt.Println(s)
}

func getBoard(w http.ResponseWriter, r *http.Request) {
	s := generator.MakeSudokuBoard("easy")

	boardJson, err := json.Marshal(s)

	var h handler.SudokuBoard
	json.Unmarshal(boardJson, &h)
	log.Println(h)
	if err != nil {
		panic(err)
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write(boardJson)
}
