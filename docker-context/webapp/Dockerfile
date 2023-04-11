FROM node:16
LABEL maintainer="woohaen88@gmail.com"

COPY ./run.sh /run.sh

EXPOSE 3000

# RUN npx create-react-app webapp --template=typescript

RUN chmod +x /run.sh

CMD ["/run.sh"]