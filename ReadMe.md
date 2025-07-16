# Pet-проект с Apache Airflow, Docker и PostgreSQL

ETL-процесс для извлечения данных с [Сайта-генератора случайных персольных данных](https://randomuser.me/api/ "Ты уверен что хочешь этого?"), их обработки и загрузки в PostgreSQL через Apache Airflow.

Проект реализует ETL-процесс :
- Extract — получает данные из randomuser.me/api/
- Transform — фильтрует и форматирует их
- Load — сохраняет в PostgreSQL
- Airflow управляет запуском и оркестровкой задач
- Docker Compose — для простого запуска всех компонентов

### Содержание:
- [Технологии](#технологии)
- [Структура проекта](#структура-проекта)
- [Требования к ПО](#требования-к-по)
- [Инструкция](#инструкция)
- [Контактная информация](#контактная-информация)

## Технологии

- Контейниризация: Docker + Docker Compose
- База данных: PostgreSQL
- Реализация ETL-процесса: Python, Redis, Apache Airflow
    в том числе:
    - Airflow-api-server 
    
        ***в прошлом webserver***
    - Airflow worker
    - Airflow-scheduler
    - Airflow-dag-processor
    - Airflow-triggerer 
    
        ***отключен потому что ETL-процесс написан не на asyncio (triggerer работает в асинхроне поэтому если что-то блокирует асинхронный цикл — ты получишь предупреждение)***
    - Requests 
    
        ***библиотека Python для выполнения HTTP-запросов*** 



## Структура проекта

```
PetProject_airflow/
├── dags/             # Папка с DAG'ами
│   └── etl_randomuser_dag.py
│
├── src/                  # Кастомные модули ETL
│   ├── extract/
│   │   └── user_extractor.py    # Модуль с функцией которая получает данные
│   ├── transform/
│   │   └── user_transformer.py  # Модуль с функцией которая обрабатывает данные
│   ├── load/
│   │   └── user_loader.py       # Модуль с функцией которая загружает данные
│   ├── utils/
│   │   └── logger.py            # Модуль c настройкой кастомного вывода логов
│   └── config/
│       └── settings.py          # Модуль с постоянными переменными
│
├── logs/                 # Папка под логи
├── requirements.txt      # Зависимости Python
├── docker-compose.yml    # Docker Compose конфигурация
├── Dockerfile            # Инструкции для Airflow контейнера
├── .env.sample           # Пример переменных окружения
├── .gitignore            # gitignore
└── README.md             # Это README
```

## Требования к ПО

- Docker, Docker Compose ***[Скачать](https://docs.docker.com/get-started/get-docker/ "В Docker Desktop уже все есть")***
- Git ***[Скачать](https://git-scm.com/downloads)***

## Инструкция

1. Клонировать репозиторий:
```bash
git clone https://github.com/MonkeysTower/PetProjectAirflow.git
cd PetProjectAirflow/
```

2. Создать .env:
    - Скопривать .env.sample
    - Отредактировать перменные внутри него под себя 
    
        ***Стоит отметить что \_AIRFLOW\_WWW\_USER\_USERNAME \_AIRFLOW\_WWW\_USER\_PASSWORD будут использоваться для входа на платформу Airflow***

3. Собрать контейнеры:
```cmd
docker-compose up
```
или
```cmd
docker-compose up -d
```
***Подождать все равно придется***

4. Зайти на платформу Airflow 
```https
https://localhost:{8081 или указаный вами в .env}
```

5. Запустить DAG

## Контактная информация
Если остались какие-то вопросы или предложения, не стесняйтесь свяжитесь со мной:
 - Email: Trifandre@yandex.ru
 - GitHub: <https://github.com/MonkeysTower/>
