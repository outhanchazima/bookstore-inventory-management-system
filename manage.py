import os
from flask.cli import FlaskGroup

from app.src import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()