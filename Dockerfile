# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем gosu
RUN set -eux; \
	apt-get update; \
	apt-get install -y gosu; \
	rm -rf /var/lib/apt/lists/*; \
	gosu nobody true

# Создаем непривилегированного пользователя
RUN groupadd -r myuser && useradd -r -g myuser myuser12

# Установка утилиты ps для просмотра запущенных процессов
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Установка утилиты ncat для проверки доступности порта postgres
RUN apt-get update && apt-get install -y ncat

# Устанавливаем зависимости
RUN pip install Flask
RUN pip install psycopg2
RUN pip install flask_sqlalchemy

# Копируем файл приложения в контейнер
COPY src/server.py /
COPY src/create_db.py /
COPY src/models/user.py /models/
COPY log/app.log /log/

# Копируем entrypoint-скрипт в контейнер
COPY ./script/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Задание 4. Установка для запуска созданного пользователя
# USER myuser12

# Задание 4, 5. Определяем команду для запуска entrypoint-скрипта при старте контейнера
ENTRYPOINT ["/entrypoint.sh"]
