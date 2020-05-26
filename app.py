from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister, Users
from resources.item import ItemList, Item
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'hooman'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # create /auth endpoint automatically.

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Users, '/users')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from project.db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
