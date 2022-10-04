from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from app import db, app
from game.models import Game, Sale, Store

game_store = Blueprint('game_store', __name__)
sucess = {"result": 200}


@game_store.route('/')
@game_store.route('/home')
def home():
    return "Welcome to the Games Store DS."


class GameView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            games = Game.query.paginate(page, 10).items
            res = {}
            for game in games:
                res[game.id] = {
                    'name': game.name,
                    'studio': game.studio,
                    'image': game.image,
                    'console': game.console,
                    'category': game.category,
                    'price': game.price
                }
        else:
            game = Game.query.filter_by(id=id).first()
            if not game:
                abort(404)
            res = {
                'name': game.name,
                'studio': game.studio,
                'image': game.image,
                'console': game.console,
                'category': game.category,
                'price': game.price
            }
        return jsonify(res)

    def post(self):

        data = request.json
        image_ = data['image'] if 'image' in data else None
        new_game = Game(name=data['name'], studio=data['studio'], image=image_, console=data['console'],
                        category=data['category'], price=data['price'])
        # db.session.add(new_game)
        # db.session.commit()
        return new_game.fs_get_delete_put_post(None)

    def put(self):
        data = request.json
        print(data['price'])
        image_ = data['image'] if 'image' in data else None
        """
        updated_game = Game.query.filter_by(id=data['id']).first()
        updated_game.name = data['name']
        updated_game.studio = data['studio']
        updated_game.image = image_
        updated_game.console = data['console']
        updated_game.category = data['category']
        updated_game.price = data['price']
        db.session.commit()
        """
        updated_game = Game(name=data['name'], studio=data['studio'], image=image_, console=data['console'],
                            category=data['category'], price=data['price'])

        return updated_game.fs_get_delete_put_post(data['id'])

    def delete(self, id):
        Game.query.filter_by(id=id).delete()
        db.session.commit()
        return sucess


class SaleView(MethodView):
    def post(self):
        data = request.json
        new_sale = Sale(game_id=data['game_id'], user_id=data['user_id'],
                        amount=data['amount'], price=data['price'])
        new_sale.fs_get_delete_put_post(None)

        new_store = Store(amount=data['amount'], price=data['price'])
        return new_store.fs_get_delete_put_post(None)

    def get(self, id=None, page=1):
        if not id:
            sales = Sale.query.paginate(page, 10).items
            res = {}
            for sale in sales:
                res[sale.id] = {
                    'game_id': sale.game_id,
                    'user_id': sale.user_id,
                    'amount': sale.amount,
                    'price': sale.price
                }
        else:
            return Sale.fs_get_delete_put_post()


game_view = GameView.as_view('game_view')
sale_view = SaleView.as_view('sale_view')

app.add_url_rule(
    '/game/', view_func=game_view, methods=['GET', 'POST', 'PUT']
)
app.add_url_rule(
    '/game/<int:id>', view_func=game_view, methods=['GET', 'DELETE']
)
app.add_url_rule(
    '/sale/', view_func=sale_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/sale/<int:id>', view_func=sale_view, methods=['GET']
)