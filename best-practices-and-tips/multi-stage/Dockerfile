FROM golang:alpine as build
WORKDIR /go
COPY hello.go .

RUN go build hello.go 

FROM scratch
COPY --from=build /go .
USER 1000:1000
ENTRYPOINT [ "/hello" ]
