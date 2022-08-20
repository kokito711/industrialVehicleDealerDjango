import json

from ..models import User


class UserNotValidException(Exception):
    pass


def to_json_dict(user):
    return dict(userCode=user.user_code, name=user.name, surnames=user.surnames)


def get_all_users():
    users = User.objects.all()
    if len(users) == 0:
        return "[]"
    else:
        return list(map(lambda user: to_json_dict(user), users))


def validate_user(user):
    if user['userCode'] is None:
        raise UserNotValidException('User code cannot be empty')
    if user['name'] is None or len(user['name']) == 0:
        raise UserNotValidException('User name cannot be empty')
    if user['surnames'] is not None and len(user['surnames']) == 0:
        raise UserNotValidException('User surnames cannot be blank')
    if user['pwd'] is None or len(user['pwd']) == 0:
        raise UserNotValidException('User pwd cannot be empty')


def create_new_user(body):
    user = json.loads(body)
    validate_user(user)
    new_user = User(user['userCode'], user['name'], user['surnames'], user['pwd'])
    new_user.save()
    return to_json_dict(new_user)
