from app import app
from app import db
from app.models import User, Casa, Led


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Casa': Casa, 'Led': Led}
