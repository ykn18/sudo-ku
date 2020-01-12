FROM golang:1.13.3-alpine3.11
WORKDIR /go/src/statistic_server
RUN go get -d -v  github.com/ykn18/sudo-ku/utils && \ 
go get -d -v go.mongodb.org/mongo-driver/bson && \
go get -d -v go.mongodb.org/mongo-driver/bson/primitive && \
go get -d -v go.mongodb.org/mongo-driver/mongo && \
go get -d -v go.mongodb.org/mongo-driver/mongo/options && \
go get -d -v github.com/gorilla/mux 

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o server .

FROM alpine:latest  
WORKDIR /root/
COPY --from=0 /go/src/statistic_server/ .
RUN chmod +x server
CMD ["./server"]