FROM nginx:1.23.3-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY ./default.conf /etc/nginx/conf.d/default.conf 
#We do it to replace default config file with own custom in this directry.