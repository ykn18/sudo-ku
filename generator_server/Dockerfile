FROM golang:1.13.3
WORKDIR /go/src/game_server
RUN go get -d -v github.com/ykn18/sudo-ku/board/model && \ 
go get -d -v go.mongodb.org/mongo-driver/bson && \
go get -d -v go.mongodb.org/mongo-driver/bson/primitive && \
go get -d -v go.mongodb.org/mongo-driver/mongo && \
go get -d -v go.mongodb.org/mongo-driver/mongo/options && \
go get -d -v github.com/gorilla/mux  && \
go get -d -v github.com/ykn18/sudo-ku/utils

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o server .

FROM alpine:latest  
WORKDIR /root/
COPY --from=0 /go/src/game_server/ .
RUN chmod +x server
CMD ["./server"]