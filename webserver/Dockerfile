FROM node:20.12.2-buster-slim

COPY ./docker-entrypoint /docker-entrypoint
WORKDIR /usr/src/app
ENV WATCHPACK_POLLING=true
ENV NODE_ENV development

COPY ./app/package*.json ./
RUN npm install
COPY ./app .

ENTRYPOINT [ "/docker-entrypoint" ]
