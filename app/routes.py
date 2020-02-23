import pyfirmata
from flask import render_template, flash, redirect, url_for

from app import app
from app import board
from app.forms import LedControl

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/led', methods=['GET', 'POST'])
def led():
    form = LedControl()

    if form.validate_on_submit():
        if int(form.estado_pin.data) == 1:
            board.digital[int(form.casa.data)].write(1)
        else:
            board.digital[int(form.casa.data)].write(0)

    return render_template('led.html', title='Led Control', form=form)

