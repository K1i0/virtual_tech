# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
RUN pip install Flask

# Копируем файл приложения в контейнер
COPY src/server.py /

# Определяем команду для запуска приложения при старте контейнера
CMD ["python", "server.py"]
