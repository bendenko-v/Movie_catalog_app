from contextlib import suppress

from sqlalchemy.exc import IntegrityError

from project.config import config
from project.models import Movie, Director, Genre
from project.server import create_app
from project.setup.db import db, models
from project.utils import read_json


def load_data(data: list[dict[str, any]], model: type[models.Base]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: dict[str, list[dict[str, any]]] = read_json("fixtures.json")

    app = create_app(config)

    with app.app_context():
        load_data(fixtures['movies'], Movie)
        load_data(fixtures['directors'], Director)
        load_data(fixtures['genres'], Genre)

        with suppress(IntegrityError):
            db.session.commit()
