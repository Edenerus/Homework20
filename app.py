from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.movies import movies_ns
from views.genres import genres_ns
from views.directors import directors_ns
from create_data import create_db_in_memory


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    configure_app(application)
    return application


def configure_app(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    create_data(application)


def create_data(application):

    with application.app_context():
        create_db_in_memory()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run(host="localhost", debug=True)
