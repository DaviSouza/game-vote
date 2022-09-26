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
