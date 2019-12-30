package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"strings"
	"time"

	"github.com/ykn18/sudo-ku/board/generator"

	"github.com/ykn18/sudo-ku/board/model"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"

	"github.com/gorilla/mux"
	"github.com/ykn18/sudo-ku/utils"
)

var client *mongo.Client

var serverSecretKey = "serversecretkey"

type SudokuEntry struct {
	ID         primitive.ObjectID `json:"_id,omitempty" bson:"_id,omitempty"`
	Board      [9][9]int          `json:"board,omitempty" bson:"board,omitempty"`
	Solution   [9][9]int          `json:"solution,omitempty" bson:"solution,omitempty"`
	Difficulty string             `json:"difficulty,omitempty" bson:"difficulty,omitempty"`
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	clientOptions := options.Client().ApplyURI("mongodb://root:toor@mongo:27017/sudo-ku?authSource=admin")
	client, _ = mongo.Connect(ctx, clientOptions)
	rand.Seed(time.Now().UnixNano())

	for i := 0; i < 3; i++ {
		insertSudokuDB(generator.MakeSudokuBoard("easy"), "easy")
	}
	for i := 0; i < 3; i++ {
		insertSudokuDB(generator.MakeSudokuBoard("medium"), "medium")
	}
	for i := 0; i < 3; i++ {
		insertSudokuDB(generator.MakeSudokuBoard("hard"), "hard")
	}
	r := mux.NewRouter()
	r.HandleFunc("/board/difficulty={difficulty}", getBoard)
	http.ListenAndServe(":7070", r)
}

func getBoard(w http.ResponseWriter, r *http.Request) {
	splittedAuth := strings.Split(r.Header.Get("Authentication"), " ")
	token := splittedAuth[1]

	valid, err := utils.VerifyToken(token, serverSecretKey)
	if valid && (err == nil) {
		w.Header().Set("Content-Type", "application/json")
		vars := mux.Vars(r)

		s := getSudokuDB(vars["difficulty"])
		boardJson, err := json.Marshal(s)

		if err != nil {
			panic(err)
		}

		w.WriteHeader(http.StatusOK)
		w.Write(boardJson)
	} else {
		w.WriteHeader(http.StatusUnauthorized)
		w.Write([]byte("Unauthorized!"))
	}
}

func insertSudokuDB(s model.SudokuBoard, diff string) {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	var e SudokuEntry
	e.Board = s.Board
	e.Solution = s.Solution
	e.Difficulty = diff

	collection := client.Database("sudo-ku").Collection("boards")

	result, _ := collection.InsertOne(ctx, e)
	fmt.Println(result)
}

func getSudokuDB(diff string) (s model.SudokuBoard) {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	collection := client.Database("sudo-ku").Collection("boards")

	n, _ := collection.CountDocuments(ctx, bson.M{"difficulty": diff})
	options := options.Find()
	options.SetLimit(1)
	options.SetSkip(int64(rand.Intn(int(n - 1))))

	var e SudokuEntry
	cur, _ := collection.Find(ctx, bson.M{"difficulty": diff}, options)
	for cur.Next(ctx) {
		err := cur.Decode(&e)
		if err != nil {
			log.Fatal("Error on Decoding the document", err)
		}
	}
	s.Board = e.Board
	s.Solution = e.Solution

	return s
}
