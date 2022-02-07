from flask.cli import FlaskGroup

from app import app, blueprint

app.register_blueprint(blueprint)

app.app_context().push()

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()