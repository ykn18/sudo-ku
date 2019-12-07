package main

import (
	"context"
	"encoding/json"
	"log"
	"math/rand"
	"net/http"
	"sudo-ku/board/model"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"

	"github.com/gorilla/mux"
)

var client *mongo.Client

type SudokuEntry struct {
	ID         primitive.ObjectID `json:"_id,omitempty" bson:"_id,omitempty"`
	Board      [9][9]int          `json:"board,omitempty" bson:"board,omitempty"`
	Solution   [9][9]int          `json:"solution,omitempty" bson:"solution,omitempty"`
	Difficulty string             `json:"difficulty,omitempty" bson:"difficulty,omitempty"`
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	clientOptions := options.Client().ApplyURI("mongodb://localhost:27017")
	client, _ = mongo.Connect(ctx, clientOptions)
	rand.Seed(time.Now().UnixNano())

	r := mux.NewRouter()
	r.HandleFunc("/board/difficulty={difficulty}", getBoard)
	http.ListenAndServe(":7070", r)
}

func getBoard(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	vars := mux.Vars(r)

	s := getSudokuDB(vars["difficulty"])

	boardJson, err := json.Marshal(s)

	if err != nil {
		panic(err)
	}

	w.WriteHeader(http.StatusOK)
	w.Write(boardJson)
}

/*
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
*/

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
