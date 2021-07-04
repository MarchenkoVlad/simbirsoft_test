# Приложение Quiz

[Ссылка на общее описание тестовое задания](https://yadi.sk/i/F4eBBIin1a4AZA)

## Почта для вопросов и результатов выполнения тестового
[internship.web@simbirsoft.com](internship.web@simbirsoft.com)

## Общий функционал
Приложение, которое позволяет пользователю пройти тестирование по вопросам с
заданными вариантами ответа, проверяет ответы и показывает пользователю результат.
Ответ на вопрос считается правильным, если пользователь выбрал все правильные варианты ответа. Если пользователь выбрал не все правильные варианты, либо лишние варианты - вопрос считается неправильным.

## Основные технологии
* Python
* Django
* Docker Compose

## ВАЖНО
Для облегчения тестирования необходимо использовать для расчета результата теста существующие наработки:
* Классы DTO описанные в `dto.py`
* Класс `QuizResultService` и его метод `get_result` описанные в `services.py `

Метод `get_result` сервиса `QuizResultService` должен возращать `float` с точностью до двух знаков после запятой, округление по стандартным правилам. Диапазон допустимых значений: от 0 до 1 включительно, где 0 - это 0% прохождения теста, а 1 - 100%.

**Весь остальной фунционал сервиса (фронт, хранение данных, роутинг и т.д.) на усмотрение разработчика.**

### Пример расчета результатов
Допустим, тест имеет три вопроса. В каждом вопросе четыре варианта ответа.
* Первый вопрос имеет один правильный результат A
* Второй вопрос имеет два правильных результата B и C
* Третий вопрос имеет один правильный результат D

#### Кейс 1
Ответы пользователя:
1. A
2. B, C
3. D

Резутальт: 1

#### Кейс 2
Ответы пользователя:
1. A
2. B
3. D

Резутальт: 0.67

#### Кейс 3
Ответы пользователя:
1. A
2. A
3. A

Резутальт: 0.33

#### Кейс 4
Ответы пользователя:
1. A
2. A, B, C
3. D

Резутальт: 0.67

#### Кейс 5
Ответы пользователя:
1. A, D
2. B, C
3. D

Резутальт: 0.67

### Ограничения
* Запрещено вносить изменения в классы DTO описанные в `dto.py`
* Запрещено менять конструктор класса `QuizResultService` и тип возращаемого значения метода `get_result`


### Команды Docker'а
Чтобы поднять заготовку приложения
```sh
docker-compose up -d
```

Чтобы выполнить тесты
```sh
docker-compose exec web python manage.py test
```

Чтобы проверить стиль кода
```sh
docker-compose exec web pycodestyle .
```

### Для проверки
После того как ТЗ будет выполненно рекомендуем развернуть проект с нуля в отдельной папке и поднять приложение, чтобы проверить все ли новые зависимости проекта правильно установились и развернулись, будь то СУБД или компоненты приложения.

### Комментарии по выполнению ТЗ
Тут пишите всю информацию по выполнению ТЗ которую считаете необходимым упомянуть.
Команды докера:

проверка стиля кода

```docker-compose exec web pycodestyle application```

запуск 

```docker-compose up -d```

тесты

```docker-compose exec web python manage.py test```

Команды для запуска без докера:

создание окружения и установка зависимостей:

```virtualenv --python=python3 env```

```source env/bin/activate```

```pip3 install -r requirements.txt```

подготовка данных и запуск приложения

```python3 manage.py makemigrations```

```python3 manage.py migrate ```

```python3 manage.py loaddata questions.json``` 

```python3 manage.py loaddata choices.json``` 

```python3 manage.py runserver 0.0.0.0:8000```

тесты

```python3 manage.py test```
