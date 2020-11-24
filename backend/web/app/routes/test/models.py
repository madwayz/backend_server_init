from app import example
from flask_restplus import fields

user = example.model('CreateUser', {
    'username': fields.String('madwayz'),
    'firstname': fields.String('Роман'),
    'surname': fields.String('Николенко')
})

user_data = example.inherit('GetUser', user, {
    'ID': fields.Integer(1)
})

user_created = example.model('UserCreated', {'message': fields.String('User is created')})
user_updated = example.model('UserUpdated', {'message': fields.String('User has been updated')})
user_deleted = example.model('UserDeleted', {'message': fields.String('User has been deleted')})
