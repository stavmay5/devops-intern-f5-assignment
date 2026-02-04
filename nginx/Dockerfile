FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /var/www/html/index.html

EXPOSE 8080 8081

CMD ["nginx", "-g", "daemon off;"]
