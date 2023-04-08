FROM node:16-alpine

COPY . . 

RUN yarn

RUN yarn build

EXPOSE 3500

CMD ["yarn", "serve"]