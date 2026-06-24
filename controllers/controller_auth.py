from models.model_user import UserModel


class AuthController:

    @staticmethod
    def login(username, password):
        return UserModel.login(username, password)