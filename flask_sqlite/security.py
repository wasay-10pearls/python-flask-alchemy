from hmac import compare_digest
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.get_user_by_username(username)
    if user and compare_digest(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.get_user_by_id(user_id)