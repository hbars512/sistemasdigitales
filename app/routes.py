# import pyfirmata
from flask import render_template, flash, redirect, url_for
from flask import request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.models import User, Casa
from app.forms import LedControl
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.forms import RegCasa, RegLed, RegSensor
# from app import board

@app.route('/')
@app.route('/index')
@login_required
def index():
    if not current_user.is_authenticated:
        return render_template('index.html', title='Home')
    user_id = current_user.get_id()
    user = User.query.get(user_id)
    casas = Casa.query.filter_by(propietario=user)

    return render_template('index.html', title='Home', casas=casas)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Ingresar', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/ledcontrol', methods=['GET', 'POST'])
@login_required
def led():
    form = LedControl()

    if form.validate_on_submit():
        # if int(form.estado_pin.data) == 1:
        #     board.digital[int(form.casa.data)].write(1)
        # else:
        #     board.digital[int(form.casa.data)].write(0)
        pass

    return render_template('led.html', title='Led Control', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Felicidades, tu estas registrado ahora!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registro', form=form)


@app.route('/regcasa', methods=['GET', 'POST'])
@login_required
def regcasa():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    user_id = current_user.get_id()
    form = RegCasa()
    user = User.query.get(user_id)
    if form.validate_on_submit():
        home = Casa(address=form.address.data, propietario=user)
        db.session.add(home)
        db.session.commit()
        flash('Felicidades, has registrado tu casa!')
        return redirect(url_for('index'))
    return render_template('regcasa.html', title='Registro casa', user=user, form=form)


@app.route('/casa')
@login_required
def casa():
    casa_id = request.args.get('cid')
    home = Casa.query.get(casa_id)
    return render_template('casa.html', casa=home)
