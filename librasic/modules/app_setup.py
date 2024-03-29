import os

from librasic import app, db
from librasic.imports.imports import Migrate

# app set-up


def setup_app_config():
    """
    Set up the application configuration.
    """
    # Use an environment variable for the database URI if it exists, otherwise use a default value
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URI", "sqlite:///librasic.db"
    )

    app.config.from_prefixed_env()


migrate: Migrate


def setup_app_db():
    """
    Set up the application database.
    """
    global migrate
    with app.app_context():
        db.create_all()
    migrate = Migrate(app, db)


def reset_database():
    """
    Reset the database by dropping all tables and then creating them again.
    """
    global db
    with app.app_context():
        db.drop_all()
        db.create_all()


# storing env vars
ENV_VARS: dict = {}


def setup_app_env_vars():
    """
    Set up the application environment variables.
    """
    global ENV_VARS
    # Use an environment variable for the default rent fee if it exists, otherwise use a default value
    DEFAULT_RENT_FEE = {"DEFAULT_RENT_FEE": int(os.getenv("DEFAULT_RENT_FEE", "20"))}
    ENV_VARS.update(DEFAULT_RENT_FEE)
