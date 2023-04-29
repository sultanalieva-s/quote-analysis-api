# Kanye quote analysis API
При GET запросе делает 10 последовательных http запросов в сервис Kanye Rest https://api.kanye.rest/
Получaeт 10 цитат
Небольшой анализ текста для каждой цитаты отдельно:
Подсчитывает общее количество букв
Посчитывает количество гласных и согласных
Подсчитывает общее количество повторений каждой буквы. Например в строке “Арарат” 3 буквы “а”, две буквы “р” и одна “т”.
Посчитывает среднюю длину всех слов в цитате
Фиксирует 3 самых длинных слова
Сохраняет в базу данных цитату и анализ выше, если данная цитата получена впервые. Т.е. в базе данных должны быть только уникальные цитаты с их данными анализа.
Покрытие юнит тестами.

## API Documentation
Postman Collection: https://www.getpostman.com/collections/c7f197a93c2adcd6c5aa
Swagger Docs: http://127.0.0.1:8000/api/v1/docs/

## How to Run Locally
From project root directory run `docker-compose up`. If you want to run the app on the background
run the command `docker-compose up -d`.

!! Make sure you have applied initial migrations before you go to localhost/kanye-sayings/.
This can be done with commands: `docker exec -it containername bash` and `./manage.py migrate`.
!!

To list containers and see their status run the command `docker-compose ps`.
To stop containers without deleting them run `docker-compose stop`.
To stop and delete the containers run `docker-compose down`.

## How to Make Migrations
Ensure that the container is running and use the following commands: `docker exec -it <your-container_name> bash`.
Now that you inside the container run the commands: `./manage.py makemigrations` and `./manage.py migrate`

## Unit Testing
To run tests you should go inside container via command `docker exec -it <your-container_name> bash`.
Then run tests via `./manage.py test`

## Notes about Time Complexity of Analysis Functions
1. count_total_letters function's time complexity is linear due to for loop which counts every letter
2. count_average_word_length function runs in O(n)
3. get_longest_words function runs in O(n)
4. count_repetitions function runs in O(n) to loop a string, and for counting letters it is O(1) because I use a dict, which is a hashtable.
