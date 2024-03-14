import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Устанавливаем соединение с postgres
connection = psycopg2.connect(
    user="postgres",
    password="admin",
    host="postgres",  # Здесь указываем имя сервиса PostgreSQL из docker-compose
    port="5432"  # Используем порт контейнера postgres (внутренний)
)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операций с базой данных
cursor = connection.cursor()

# Проверяем наличие базы данных
cursor.execute("SELECT datname FROM pg_database WHERE datname='sql_test'")
if not cursor.fetchone():
    # Создаем базу данных, только если она еще не существует
    cursor.execute("CREATE DATABASE sql_test")
    print("База данных 'sql_test' успешно создана.")
else:
    print("База данных 'sql_test' уже существует.")

# Закрываем соединение
cursor.close()
connection.close()
