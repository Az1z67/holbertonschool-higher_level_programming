FROM alpine:latest

RUN apk add --no-cache curl

RUN mkdir -p /app

COPY config.txt

WORKDIR /app

CMD ["echo", "Container is set up"]

