# import pyfirmata
from flask import render_template, flash, redirect, url_for

from app import app
# from app import board
from app.forms import LedControl
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.nombre.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Ingresar', form=form)


@app.route('/led', methods=['GET', 'POST'])
def led():
    form = LedControl()

    if form.validate_on_submit():
        # if int(form.estado_pin.data) == 1:
        #     board.digital[int(form.casa.data)].write(1)
        # else:
        #     board.digital[int(form.casa.data)].write(0)
        pass

    return render_template('led.html', title='Led Control', form=form)

