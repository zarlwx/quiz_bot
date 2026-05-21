# 🤖 QuizBot — Survey bot with saved results

## Description
A Django web application with a Telegram bot for completing surveys.
The user opens the website or contacts the bot, completes the survey, and sees the results.
All responses and sessions are stored in a SQLite database.

## Technologies
- Python 3
- Django 4.2
- SQLite (база данных)
- Bootstrap 5 (интерфейс)
- Telegram Bot API

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/твой_ник/quiz_bot.git
cd quiz_bot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Apply migrations**
```bash
python manage.py migrate
```

**4. Create a superuser**
```bash
python manage.py createsuperuser
```

**5. Start the server**
```bash
python manage.py runserver
```

## Launching a Telegram bot
```bash
cd telegrambot
python bot.py
```

## Addresses
- Site: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin
- Telegram: @myquizproject_bot

## Bot commands
| Command  | Description                    |
|----------|--------------------------------|
| /start   | Greetings and list of commands |
| /quizzes | List of available surveys      |
| /quiz_1  | Survey Information             |
| /help    | Help                           |

## Project structure
```
quiz_bot/
├── quiz_bot/            # settings Django
│   ├── settings.py
│   └── urls.py
├── surveys/             # main application
│   ├── models.py        # models BD (Quiz, Question, Answer, UserSession, UserResponse)
│   ├── views.py         # page logic
│   ├── urls.py          # routes
│   └── templates/       # HTML templates
│       └── surveys/
│           ├── base.html
│           ├── home.html
│           ├── quiz.html
│           └── results.html
├── telegrambot/
│   └── bot.py           # Telegram bot
├── manage.py
├── requirements.txt
└── README.md
```

## Possibilities
- View the list of surveys on the main page
- Step-by-step survey completion with a progress bar
- Saving all answers and results in the database
- Viewing the results with an analysis of correct/incorrect answers
- Managing Polls via Django Admin
- Telegram bot for accessing surveys
