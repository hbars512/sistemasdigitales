from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectField, StringField
from wtforms import PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
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
