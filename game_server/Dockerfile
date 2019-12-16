FROM golang
WORKDIR /go/src/game_server
RUN go get -d -v github.com/ykn18/sudo-ku/board/handler
RUN go get -d -v github.com/ykn18/sudo-ku/board/model
RUN go get -d -v github.com/ykn18/sudo-ku/game_server/communication
RUN go get -d -v github.com/ykn18/sudo-ku/game_server/utils  
COPY . .
RUN go build -o server .

FROM alpine:latest  
WORKDIR /root/
COPY --from=0 /go/src/game_server .
CMD ["./server"]