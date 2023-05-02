# routes.py

from lesco import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from lesco.models import User, PhoneNumber, ReferenceNumber
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from lesco.forms import LoginForm, SignupForm
from flask_mail import Mail, Message

@app.route('/')
def home():
    return render_template("home.html")


def load_user(user_id):
    return User.query.get(int(user_id))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        # Check if user exists in database
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html', form=form)

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = SignupForm()
    if form.validate_on_submit():
        # Check if user already exists in database
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('An account with that email address already exists.', 'danger')
            return redirect(url_for('signup'))

        # Create new user
        new_user = User(name=form.name.data,
                        email=form.email.data,
                        password=generate_password_hash(form.password.data, method='sha256'),
                        phone_numbers=[PhoneNumber(number=form.phone_number.data)],
                        reference_numbers=[ReferenceNumber(batch_no=form.batch_no.data,
                                                           sub_div=form.sub_div.data,
                                                           ref_no=form.ref_no.data)])
        db.session.add(new_user)
        db.session.commit()

        # Send welcome email to new user
        msg = Message('Welcome to Lesco!', sender=app.config['MAIL_USERNAME'], recipients=[form.email.data])
        msg.body = f'Dear {form.name.data},\n\nWelcome to Lesco! Your account has been created successfully.\n\nRegards,\nThe Lesco Team'
        mail.send(msg)

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)