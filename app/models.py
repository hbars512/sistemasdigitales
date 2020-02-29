from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db
from app import login

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    casas = db.relationship('Casa', backref='propietario', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Casa(db.Model):
    __tablename__ = 'casas'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    leds = db.relationship('Led', backref='domicilio', lazy='dynamic')
    sensores = db.relationship('Sensor', backref='domicilio', lazy='dynamic')

    def __repr__(self):
        return '<Casa {}>'.format(self.address)


class Led(db.Model):
    __tablename__ = 'leds'
    id = db.Column(db.Integer, primary_key=True)
    puerto = db.Column(db.Integer)
    casa_id = db.Column(db.Integer, db.ForeignKey('casas.id'))
    estados_led = db.relationship('EstadoLed', backref='led', lazy='dynamic')

    def __repr__(self):
        return '<Led {}>'.format(self.puerto)


class Sensor(db.Model):
    __tablename__ = 'sensores'
    id = db.Column(db.Integer, primary_key=True)
    puerto = db.Column(db.Integer)
    casa_id = db.Column(db.Integer, db.ForeignKey('casas.id'))
    estados_sensor = db.relationship('EstadoSensor', backref='sensor', lazy='dynamic')

    def __repr__(self):
        return '<Sensor {}>'.format(self.puerto)


class EstadoLed(db.Model):
    __tablename__ = 'estados_led'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    led_id = db.Column(db.Integer, db.ForeignKey('leds.id'))

    def __repr__(self):
        return '<EstadoLed {} - {}>'.format(self.status, self.timestamp)


class EstadoSensor(db.Model):
    __tablename__ = 'estados_sensor'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensores.id'))

    def __repr__(self):
        return '<EstadoSensor {} - {}>'.format(self.status, self.timestamp)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
