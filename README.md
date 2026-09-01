# 🚀 SQLAlchemy Multi-DB Async Playground

Учебный пет-проект, демонстрирующий организацию асинхронного взаимодействия с несколькими реляционными базами данных (**PostgreSQL** и **MySQL**) с использованием **SQLAlchemy 2.0**, **AsyncIO** и современного менеджера пакетов **uv**.

---

## 🛠 Технологический стек

* **Язык**: Python 3.11+
* **ORM**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (AsyncIO API)
* **Драйверы БД**: `asyncpg` (PostgreSQL), `aiomysql` (MySQL)
* **Менеджер пакетов и окружения**: [uv](https://github.com/astral-sh/uv)
* **Контейнеризация**: Docker & Docker Compose

---

## 📌 Основные возможности и паттерны

1. **Multi-Engine & Multi-Session**: Настройка независимых асинхронных движков (`AsyncEngine`) и фабрик сессий (`async_sessionmaker`) для различных СУБД.
2. **Modern Declarative Mapping**: Использование синтаксиса SQLAlchemy 2.0 с анотациями типов `Mapped[...]` и `mapped_column()`.
3. **Паттерн CRUD / Repository**: Выделение логики работы с базой данных в изолированные функции (`create_user`, `list_users`).
4. **Ресурсный менеджмент**: Корректное использование асинхронных контекстных менеджеров (`async with`) и явный вызов `.dispose()` для закрытия пула соединений.

---

## 📁 Структура проекта

```text
sqlalchemy_multi_db/
├── db/
│   ├── __init__.py
│   ├── base.py         # Базовый класс DeclarativeBase
│   ├── mysql.py        # Инициализация и подключение к MySQL
│   ├── postgres.py     # Инициализация и подключение к PostgreSQL
│   ├── crud.py         # Универсальные операции (CRUD)
│   └── models/
│       ├── __init__.py
│       └── user.py     # ORM-модель пользователя
├── main.py             # Точка входа в приложение
├── docker-compose.yml  # Запуск PostgreSQL и MySQL в контейнерах
├── pyproject.toml      # Зависимости проекта
└── README.md
