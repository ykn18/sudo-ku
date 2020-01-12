FROM golang:1.13.3
WORKDIR /go/src/game_server
RUN go get -d -v github.com/ykn18/sudo-ku/board/handler && \
go get -d -v github.com/ykn18/sudo-ku/board/model && \
go get -d -v github.com/ykn18/sudo-ku/game_server/communication && \
go get -d -v github.com/ykn18/sudo-ku/utils 
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o server .

FROM alpine:latest  
WORKDIR /root/
COPY --from=0 /go/src/game_server/ .
RUN chmod +x server
CMD ["./server"]