from flask import Flask

from config import env
from db import db, migrate


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = env.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    return app

app = create_app()

@app.get('/')
def home():
    return "Welcome!!!"


if __name__ == "__main__":
    app.run(
        host=env.host,
        port=env.port,
        debug=True,
    )
