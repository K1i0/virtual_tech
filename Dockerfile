# Используем официальный образ Python
FROM python:3.9-slim


# Устанавливаем gosu
# RUN apt-get update && apt-get install -y gosu && rm -rf /var/lib/apt/lists/*
RUN set -eux; \
	apt-get update; \
	apt-get install -y gosu; \
	rm -rf /var/lib/apt/lists/*; \
# verify that the binary works
	gosu nobody true

# Создаем непривилегированного пользователя
RUN groupadd -r myuser && useradd -r -g myuser myuser12

# Установка утилиты ps для просмотра запущенных процессов
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости
RUN pip install Flask

# Копируем файл приложения в контейнер
COPY src/server.py /

# Копируем entrypoint-скрипт в контейнер
COPY ./script/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# USER myuser12

# # Определяем команду для запуска приложения при старте контейнера
# CMD ["python", "server.py"]

# Определяем команду для запуска entrypoint-скрипта при старте контейнера
ENTRYPOINT ["/entrypoint.sh"]