from app import app, db  # noqa F401
from app.models import  User, Post  # noqa F401


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
