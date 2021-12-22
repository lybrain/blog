# Run with docker-compose
1. Build containers and run them
docker-compose up -d
2. Create super user
docker exec -it blog_web_1 python manage.py createsuperuser