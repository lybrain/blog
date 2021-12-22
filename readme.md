# Run project
docker-compose up -d
# create super user
docker exec -it blog_web_1 python manage.py createsuperuser