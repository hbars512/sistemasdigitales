from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectField, StringField
from wtforms import PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Sign In')


class LedControl(FlaskForm):
    estado_pin = RadioField(
        '', choices=[('1', 'Encender'), ('0', 'Apagar')],
        validators=[DataRequired()])
    casa = SelectField(u'Numero de casa',
                       choices=[('12', 'Casa 1'), ('11', 'Casa 2'),
                                ('10', 'Casa 3'), ('9', 'Casa 4')])
    submit = SubmitField('Enviar')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repetir Contraseña',
                              validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor, use un nombre de usuario diferente')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor use una direccion de correo diferente')

class RegCasa(FlaskForm):
    address = StringField('Direccion', validators=[DataRequired()])
    submit = SubmitField('Registrar')


class RegLed(FlaskForm):
    puerto = IntegerField('Puerto', validators=[DataRequired()])


class RegSensor(FlaskForm):
    puerto = IntegerField('Puerto', validators=[DataRequired()])
