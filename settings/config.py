from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class Config(object):
    TESTING = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % str(BASE_DIR.joinpath("todo.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    pass
