from app import db
from flask_serialize import FlaskSerialize

fs_mixin = FlaskSerialize(db)


class Game(fs_mixin, db.Model):
    __tablename__ = 'game'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    studio = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String())
    console = db.Column(db.String(40))
    category = db.Column(db.String(30))
    price = db.Column(db.Float(asdecimal=True))

    __fs_create_fields__ = __fs_update_fields__ = ['name', 'studio', 'image', 'console', 'category', 'price']

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Store(fs_mixin, db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))

    __fs_create_fields__ = __fs_update_fields__ = ['game_id', 'amount']


class Order(fs_mixin, db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    user_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    price = db.Column(db.Float(asdecimal=True))

    __fs_create_fields__ = __fs_update_fields__ = ['id', 'game_id', 'user_id', 'amount', 'price']


class Rating(fs_mixin, db.Model):
    __tablename__ = 'rating'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    comment = db.Column(db.String())
    user_id = db.Column(db.Integer)
    grade = db.Column(db.Integer)

    __fs_create_fields__ = __fs_update_fields__ = ['game_id', 'user_id', 'comment', 'grade']
