from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

from game.kafka import MessageConsumer

app = Flask(__name__)
app.config.from_pyfile('game/config.py')
logging.basicConfig(level=logging.DEBUG)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from game.views import game_store
consumer = MessageConsumer()
consumer.activate_listener()

app.register_blueprint(game_store)

if __name__ == '__main__':
    app.run(debug=True)
