from app.src import app, db

from flask_migrate import Migrate
from flask_restx import Api
from flask import Blueprint


from app.src.controllers.auth_resource import api as auth_ns
from app.src.controllers.user_resource import api as user_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='BookStore Inventory System REST API',
    version='1.0',
    description='BookStore invetory api to manage book stocks',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(auth_ns, path='/auth')
api.add_namespace(user_ns, path='/user')

migrate = Migrate(app, db)
