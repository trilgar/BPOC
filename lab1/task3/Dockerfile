FROM node

RUN mkdir /app
WORKDIR /app

RUN npm install -g json-server

COPY db.json db.json

CMD ["json-server", "-H", "0.0.0.0", "-p", "3000",  "--watch", "db.json"]
