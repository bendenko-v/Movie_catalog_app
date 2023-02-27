from project.models import Favorite
from project.utils import read_json

from project.config import config
from project.server import create_app
from project.setup.db import db

if __name__ == '__main__':

    data: list[dict[str, any]] = read_json("favorites.json")
    with create_app(config).app_context():
        # db.create_all()

        for item in data:
            item['id'] = item.pop('pk')
            db.session.add(Favorite(**item))
            db.session.commit()
