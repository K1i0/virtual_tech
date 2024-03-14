from flask import Flask, request, jsonify
from models.user import db, User

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
# Устанавливаем URI для подключения к базе данных PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@postgres:5432/sql_test'

# Инициализируем SQLAlchemy с нашим приложением
db.init_app(app)

# Настройка логгера
logging.basicConfig(filename='log/app.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    # Возвращаем контент в виде строки
    return 'Hello World!'


@app.route('/users', methods=['GET'])
def get_users():
    logging.info('Recieved GET USERS request: {}, {}, {}'.format(request.method, request.url, request.data))
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])


@app.route('/users', methods=['PUT'])
def create_user():
    app.logger.info('Recieved PUT USER request: {}, {}, {}'.format(request.method, request.url, request.data))
    data = request.json
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    app.logger.info('New user added: {} {}'.format(data['name'], data['email']))
    return jsonify({'message': 'User created successfully'})


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    app.logger.info('Recieved GET USER BY ID = {} request: {}, {}, {}'.format(user_id, request.method, request.url, request.data))
    user = User.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    app.logger.info('Recieved DELETE USER BY ID = {} request: {}, {}, {}'.format(user_id, request.method, request.url, request.data))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
    with app.app_context():
        # Создаем таблицы в базе данных
        db.create_all()
    # Запуск сервера. Порт 8000, перезагрузка и вывод ошибок на странице в режиме отладки
    app.run(host='0.0.0.0', port=8000, debug=True)
