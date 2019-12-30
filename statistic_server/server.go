package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strings"
	"time"

	"github.com/ykn18/sudo-ku/utils"

	"github.com/gorilla/mux"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

const serverSecretKey = "serversecretkey"
const userSecretKey = "usersecretkey"

type MatchResult struct {
	Win       bool      `bson:"win" json:"win,omitempty"`
	MatchTime int       `bson:"matchtime" json:"matchTime,omitempty"`
	DateTime  time.Time `bson:"datetime" json:"dateTime,omitempty"`
}

type User struct {
	ID       primitive.ObjectID `bson:"_id" json:"id,omitempty"`
	Username string             `bson:"username" json:"username,omitempty"`
	Matches  []MatchResult
}

type Stats struct {
	Won     int `bson:"won" json:"won"`
	Lost    int `bson:"lost" json:"lost"`
	AvgTime int `bson:"avgtime" json:"avgTime"`
}

func (u *User) addMatchResult(matchResult MatchResult) []MatchResult {
	u.Matches = append(u.Matches, matchResult)
	return u.Matches
}

func (u User) getStatistics() Stats {
	won := 0
	lost := 0
	totTime := 0

	for _, match := range u.Matches {
		totTime += match.MatchTime
		if match.Win {
			won++
			continue
		}
		lost++
	}
	return Stats{won, lost, totTime / len(u.Matches)}
}

var client *mongo.Client

func main() {
	clientOptions := options.Client().ApplyURI("mongodb://root:toor@mongo:27017/statistics?authSource=admin")
	client, _ = mongo.Connect(context.TODO(), clientOptions)
	err := client.Ping(context.TODO(), nil)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Connected to MongoDB!")

	r := mux.NewRouter()
	r.HandleFunc("/ping", ping).Methods("GET")
	r.HandleFunc("/user/{username}/result", saveMatchResult).Methods("POST")
	r.HandleFunc("/stats", getStats).Methods("GET")
	http.ListenAndServe(":5050", r)
}

func ping(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("pong"))
}

func saveMatchResult(w http.ResponseWriter, r *http.Request) {
	collection := client.Database("statistics").Collection("users")
	vars := mux.Vars(r)
	var matchResult MatchResult
	err := json.NewDecoder(r.Body).Decode(&matchResult)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	var user User
	filter := bson.M{"username": vars["username"]}
	err = collection.FindOne(context.TODO(), filter).Decode(&user)
	if err != nil {
		user.ID = primitive.NewObjectID()
		user.Username = vars["username"]
		user.addMatchResult(matchResult)
		insertResult, err := collection.InsertOne(context.TODO(), user)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			return
		}
		fmt.Println("Inserted: ", insertResult.InsertedID)
		w.WriteHeader(http.StatusCreated)
		return
	}
	filter = bson.M{"_id": user.ID}
	update := bson.M{"$push": bson.M{"matches": matchResult}}
	res, err := collection.UpdateOne(context.TODO(), filter, update)
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		return
	}
	fmt.Println(res)
	w.WriteHeader(http.StatusOK)
}

func getStats(w http.ResponseWriter, r *http.Request) {
	collection := client.Database("statistics").Collection("users")
	token := r.Header.Get("Authorization")
	splitToken := strings.Split(token, " ")
	token = splitToken[1]
	valid, err := utils.VerifyToken(token, userSecretKey)
	if valid && (err == nil) {
		payload, err := utils.DecodeToken(token)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			return
		}
		var user User
		username := payload.Username
		filter := bson.M{"username": username}
		err = collection.FindOne(context.TODO(), filter).Decode(&user)
		if err != nil {
			w.WriteHeader(http.StatusNotFound)
			w.Write([]byte("Error, user not found"))
			return
		}
		stats := user.getStatistics()
		jsonStats, err := json.Marshal(stats)
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		w.Write(jsonStats)
		return
	}
	w.WriteHeader(http.StatusUnauthorized)
	w.Write([]byte("Error, invalid token"))
}
