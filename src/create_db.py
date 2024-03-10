import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Устанавливаем соединение с postgres
connection = psycopg2.connect(
    user="postgres",
    password="admin",
    host="localhost",  # Здесь указываем имя сервиса PostgreSQL из docker-compose
    port="5432"  # Используем порт, который проброшен из контейнера PostgreSQL
)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операций с базой данных
cursor = connection.cursor()
# Создание БД
sql_create_database = cursor.execute('create database sql_test')
# Закрываем соединение
cursor.close()
connection.close()
