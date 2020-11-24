from flask_restplus import Resource, abort
from app.routes.test.provider import Provider
from app.routes.test.models import *
from app import example

"""
ВАЖНО! В нашем случае используется ns_api, а не example.

model = example.model('Class', {'status': fields.String('Ok')})
Мы говорим, что работаем со словарём, в нём будет ключ 'status', а значение должно быть string. По дефолту "Ok"
 
@example.response(404, 'User not found') - В документации покажем, что на 404 HTTP статус код - это 'User not found'
@example.expect(model) - пример json'а, который мы ожидаем от клиента
@example.marshal_with(model) - Пример json'а, который пользователь на определённый HTTP код. 200 по дефолту.
@example.route('/path_to') - куда нужно обратиться для выполнения метода. https://example.com/api/path_to

abort(404) - вернуть ошибку 404.
api.payload - прочитать json из запроса. Работает только для POST.
"""

# TODO: Сделать парсер аргументов

users = {'user_ids': [], 'user_data': []}
counter = 1


@example.route('/user/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
@example.route('/user', methods=['POST'])
class User(Resource):
    @example.response(404, 'User not found')
    @example.marshal_with(user_data)
    def get(self, user_id):
        """Получить юзера по id"""
        if user_id not in users['user_ids']:
            return {'message': 'User not found'}, 404

        return {'ID': user_id, **users.get(user_id)}

    @example.expect(user)
    @example.response(201, 'User is created')
    @example.marshal_with(user_created)
    def post(self):
        """Создать юзера"""
        users['user_ids'].append(counter)
        users['user_data'].append({'ID': counter, **example.payload})
        return {'message': 'User is created'}

    @example.expect(user)
    @example.response(404, 'User not found')
    @example.response(200, 'User has been updated')
    @example.marshal_with(user_updated)
    def put(self, user_id):
        """Обновить данные юзера"""
        if user_id not in users['user_ids']:
            return {'message': 'User not found'}, 404

        for user in users['user_data']:
            if user.get('ID') != user_id:
                continue

            user.update({'ID': user_id, **example.payload})
        return {'message': 'User has been updated'}

    @example.response(404, 'User not found')
    @example.response(500, 'Some errors with deleting a user')
    @example.marshal_with(user_deleted)
    def delete(self, user_id):
        """Удалить юзера"""
        is_deleted = False

        if user_id not in users['user_ids']:
            return {'message': 'User not found'}, 404

        for user in users['user_data']:
            if user.get('ID') != user_id:
                continue

            user.pop()
            is_deleted = True

        if is_deleted:
            users['user_ids'].pop(user_id)

        if user_id in users['user_ids'] or not is_deleted:
            return {'message': 'Some errors with deleting a user'}, 500

        return {'message': 'User has been deleted'}


@example.route('/users')
class Users(Resource):
    @example.response(404, 'Users not found')
    @example.marshal_with(user_data, as_list=True)
    def get(self):
        """Получить всех юзеров"""
        if not users:
            abort(404)
        return users
