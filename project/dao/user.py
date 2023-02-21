from project.models import User
from sqlalchemy.orm import scoped_session


class UserDAO:

    def __init__(self, db_session: scoped_session) -> None:
        self._db_session = db_session

    def get_one(self, uid):
        return self._db_session.query(User).get(uid)

    def get_by_email(self, email):
        return self._db_session.query(User).filter(User.email == email).first()

    def get_all(self):
        return self._db_session.query(User).all()

    def create(self, new_user):
        entity = User(**new_user)
        self._db_session.add(entity)
        self._db_session.commit()
        return entity

    def update(self, data):
        user = self.get_one(data.get("id"))
        user.email = data.get("login")
        user.password = data.get("password")

        self._db_session.add(user)
        self._db_session.commit()

    def delete(self, uid):
        user = self.get_one(uid)
        self._db_session.delete(user)
        self._db_session.commit()
