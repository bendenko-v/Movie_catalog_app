from project.models import Movie
from project.utils import read_json

from project.config import config
from project.server import create_app
from project.setup.db import db

if __name__ == '__main__':

    data: list[dict[str, any]] = read_json("movies.json")
    with create_app(config).app_context():

        for item in data:
            item['id'] = item.pop('pk')
            db.session.add(Movie(**item))
            db.session.commit()
