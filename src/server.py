from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    # Возвращаем контент в виде строки
    return 'Hello World!'


if __name__ == '__main__':
    # Запуск сервера. Порт 8000, перезагрузка и вывод ошибок на странице в режиме отладки
    app.run(host='0.0.0.0', port=8000, debug=True)
