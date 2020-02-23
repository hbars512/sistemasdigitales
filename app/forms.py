from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired


class LedControl(FlaskForm):
    estado_pin = RadioField('', choices=[('1', 'Encender'),
                                         ('0', 'Apagar')],
                            validators=[DataRequired()])
    casa = SelectField(u'Numero de casa', choices=[('12', 'Casa 1'), ('11', 'Casa 2'),
                                                   ('10', 'Casa3'), ('9', 'Casa4')])
    submit = SubmitField('Enviar')
