FROM node:12.13.0-slim

WORKDIR /usr/src/app

COPY package.json
RUN npm install

COPY server.js

ENTRYPOINT node server.js