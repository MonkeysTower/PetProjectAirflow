from airflow.providers.postgres.hooks.postgres import PostgresHook
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def load_user(transformed_user):
    logger.info("Начинаем загрузку данных в БД через PostgresHook")

    # Подключаемся через Airflow Connection (в Web UI можно настроить)
    pg_hook = PostgresHook(postgres_conn_id='postgres')  # Имя подключения
    conn = pg_hook.get_conn()
    cur = conn.cursor()

    cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100),
                last_name VARCHAR(100),
                email VARCHAR(100),
                city VARCHAR(100),
                country VARCHAR(100),
                phone VARCHAR(20)
            );
    """)

    cur.execute("""
        INSERT INTO users (first_name, last_name, email, city, country, phone)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        transformed_user['first_name'],
        transformed_user['last_name'],
        transformed_user['email'],
        transformed_user['city'],
        transformed_user['country'],
        transformed_user['phone']
    ))

    conn.commit()
    cur.close()
    conn.close()

    logger.info("Данные успешно загружены в PostgreSQL")