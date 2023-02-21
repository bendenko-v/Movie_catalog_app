from project.tools.security import generate_password_hash, compose_passwords
from project.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO) -> None:
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        if self.dao.get_by_email(user_data['email']):
            return None
        user_data['password'] = self.generate_hash(user_data['password'])
        return self.dao.create(user_data)

    def update(self, user_data):
        if user := self.dao.get_by_email(user_data['login']):
            if self.compare_passwords(user.password, user_data['old_password']):
                user_data['password'] = self.generate_hash(user_data['password'])
                self.dao.update(user_data)
                return True
        return False

    def delete(self, uid):
        self.dao.delete(uid)

    def generate_hash(self, password):
        return generate_password_hash(password)

    def compare_passwords(self, password_hash, password):
        return compose_passwords(password_hash, password)
