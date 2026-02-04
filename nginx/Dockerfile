# Nginx Web Server Dockerfile

# Alpine-based: ~5MB vs Ubuntu's ~70MB. Trade-off: musl libc (not glibc)
FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /var/www/html/index.html

# Documentation only - actual mapping in docker-compose
EXPOSE 8080 8081

CMD ["nginx", "-g", "daemon off;"]