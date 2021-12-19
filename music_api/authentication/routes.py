from flask import Blueprint, render_template, request
from music_api.forms import UserLogInForm
from music_api.models import db, User


auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserLogInForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email,password)
        new_user = User(email, password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('signup.html', form = form)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserLogInForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email,password)
    return render_template('signin.html', form = form)