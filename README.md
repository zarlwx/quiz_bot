# 🤖 QuizBot — Бот-опросник с сохранением результатов

## Описание
Веб-приложение на Django с Telegram-ботом для прохождения опросов.
Пользователь открывает сайт или пишет боту, проходит опрос и видит результат.
Все ответы и сессии сохраняются в базе данных SQLite.

## Технологии
- Python 3
- Django 4.2
- SQLite (база данных)
- Bootstrap 5 (интерфейс)
- Telegram Bot API

## Установка

**1. Клонируй репозиторий**
```bash
git clone https://github.com/твой_ник/quiz_bot.git
cd quiz_bot
```

**2. Установи зависимости**
```bash
pip install -r requirements.txt
```

**3. Примени миграции**
```bash
python manage.py migrate
```

**4. Создай суперпользователя**
```bash
python manage.py createsuperuser
```

**5. Запусти сервер**
```bash
python manage.py runserver
```

## Запуск Telegram бота
```bash
cd telegrambot
python bot.py
```

## Адреса
- Сайт: http://127.0.0.1:8000
- Админка: http://127.0.0.1:8000/admin
- Telegram: @myquizproject_bot

## Команды бота
| Команда | Описание |
|---------|----------|
| /start | Приветствие и список команд |
| /quizzes | Список доступных опросов |
| /quiz_1 | Информация об опросе |
| /help | Помощь |

## Структура проекта
```
quiz_bot/
├── quiz_bot/            # настройки Django
│   ├── settings.py
│   └── urls.py
├── surveys/             # основное приложение
│   ├── models.py        # модели БД (Quiz, Question, Answer, UserSession, UserResponse)
│   ├── views.py         # логика страниц
│   ├── urls.py          # маршруты
│   └── templates/       # HTML шаблоны
│       └── surveys/
│           ├── base.html
│           ├── home.html
│           ├── quiz.html
│           └── results.html
├── telegrambot/
│   └── bot.py           # Telegram бот
├── manage.py
├── requirements.txt
└── README.md
```

## Возможности
- Просмотр списка опросов на главной странице
- Пошаговое прохождение опроса с прогресс-баром
- Сохранение всех ответов и результатов в БД
- Просмотр итогов с разбором правильных/неправильных ответов
- Управление опросами через Django Admin
- Telegram бот для доступа к опросам
