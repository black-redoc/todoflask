import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blueprints.todo import todo_blueprint

env = os.environ.get
db = SQLAlchemy()

if env("FLASK_DEBUG"):
    from dotenv import load_dotenv

    load_dotenv("./.flaskenv")


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    else:
        # load the instance config if it exist when not testing
        if env("FLASK_DEBUG"):
            app.config.from_object("settings.config.DevelopmentConfig")
        else:
            app.config.from_object("settings.config.ProductionConfig")

        # ensure the instance folder exists
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        # init db
        db.init_app(app)
        # register blueprints
        app.register_blueprint(todo_blueprint, url_prefix="/api/todo")

        return app
