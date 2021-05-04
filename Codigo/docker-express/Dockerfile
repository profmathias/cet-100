FROM node:14-alpine

RUN mkdir -p /docker-express
WORKDIR /docker-express

COPY . .
RUN npm install -g

EXPOSE 3000

ENTRYPOINT ["docker-express"]
