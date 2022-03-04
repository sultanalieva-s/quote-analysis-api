# reviroio-junior-python-assignment

## Documentation
Postman Collection: https://www.getpostman.com/collections/c7f197a93c2adcd6c5aa
Swagger Docs: http://127.0.0.1:8000/api/v1/docs/

## How to Run Locally
From project root directory run `docker-compose up`. If you want to run the app on the background
run the command `docker-compose up -d`.
To list containers and see their status run the command `docker-compose ps`.
To stop containers without deleting them run `docker-compose stop`.
To stop and delete the containers run `docker-compose down`.

## How to Make Migrations
Ensure that the container is running and use the following commands: `docker exec -it <your-container_name> bash`.
Now that you inside the container run the commands: `./manage.py makemigrations` and `./manage.py migrate`

## Unit Testing
To run tests you should go inside container via command `docker exec -it <your-container_name> bash`.
Then run tests via `./manage.py test`
