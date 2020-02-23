import pyfirmata
from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
board = pyfirmata.Arduino('/dev/ttyACM0')


from app import routes
