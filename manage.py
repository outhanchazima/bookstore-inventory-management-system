from flask.cli import FlaskGroup

from app import app, blueprint

app.register_blueprint(blueprint)

app.app_context().push()

cli = FlaskGroup(app)

@cli.command("test")
def unitTesting():
    """Runs the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover("app/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    cli()