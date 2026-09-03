# Family Budget Tracker

Простой backend-сервис для совместного управления семейным бюджетом.

Проект позволяет пользователям создавать комнаты, приглашать участников и вести общий учёт доходов и расходов.

## 🛠 Стек

* Python 3.12+
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic v2
* JWT
* Docker / Docker Compose

## 📌 Основные возможности

* Регистрация и авторизация пользователей
* JWT-аутентификация
* Создание комнат
* Добавление участников в комнаты
* Приглашение по уникальному коду
* Создание и управление транзакциями
* Категории доходов и расходов
* Разделение данных между комнатами

## 📂 Структура проекта

```text
family-budget-tracker/
├── routers/
├── services/
├── models/
├── schemas/
├── core/
├── database/
├── main.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🚀 Запуск

### Локальный запуск

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить приложение:

```bash
uvicorn main:app --reload
```

После запуска API будет доступно по адресу:

```text
http://localhost:8000
```

Swagger-документация:

```text
http://localhost:8000/docs
```

### Docker

Для запуска проекта через Docker Compose:

```bash
docker compose up --build
```

## 🌿 Ветки

Основная ветка разработки:

```text
develop-backend
```

Все текущие изменения backend разрабатываются в `develop-backend`.

## 🎯 Статус проекта

Проект находится в разработке.

Основной фокус — реализация и развитие backend API для семейного учёта финансов.

## 📄 Лицензия

Учебный проект.
