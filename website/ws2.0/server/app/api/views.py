from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import api
from .. import db
from ..models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm, ChangePasswordForm, \
    ChangeEmailForm, PasswordResetForm, PasswordResetRequestForm

"""
@api.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed and request.endpoint and request.blueprint != 'api' and request.endpoint != 'static':
            return redirect(url_for('api.unconfirmed'))


@api.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect('home.index')
    return render_template('auth/unconfirmed.html')

@api.route('/users/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('home.index')
            return redirect(next)
        flash('Invalid email or password')
    return render_template('auth/login.html', form=form)

@api.route('/users/logout')
@login_required
def logout():
    logout_user()
    flash('You been logged out.!')
    return redirect(url_for('home.index'))

@api.route('/users/signup', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(), password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_auth_token()
        send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)
        flash('Confirmation email has been sent to you by email submitted.')
        return redirect(url_for('api.login'))
    return render_template('auth/register.html', form=form)

"""