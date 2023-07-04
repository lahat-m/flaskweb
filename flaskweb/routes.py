from flask import render_template, url_for, flash, redirect, request
from flaskweb import app, db, bcrypt  # Importing necessary modules and packages
from flaskweb.forms import RegistrationForm, LoginForm
from flaskweb.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")  # Route decorator for the home page
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)  # Renders the home.html template and passes the 'posts' variable to it

@app.route("/about")  # Route decorator for the about page
def about():
    return render_template('about.html', title='About')  # Renders the about.html template and sets the 'title' variable to 'About'

@app.route("/register", methods=['GET', 'POST'])  # Route decorator for the register page
def register():
    if current_user.is_authenticated:  # If the current user is already authenticated, redirect to the home page
        return redirect(url_for('home'))
    form = RegistrationForm()  # Create an instance of the RegistrationForm
    if form.validate_on_submit():  # If the form is submitted and valid
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  # Hash the password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)  # Create a new User object
        db.session.add(user)  # Add the new user to the database session
        db.session.commit()  # Commit the changes to the database
        flash('Your account has been created! You are now able to log in', 'success')  # Flash a success message
        return redirect(url_for('login'))  # Redirect to the login page
    return render_template('register.html', title='Register', form=form)  # Render the register.html template with the form

@app.route("/login", methods=['GET', 'POST'])  # Route decorator for the login page
def login():
    if current_user.is_authenticated:  # If the current user is already authenticated, redirect to the home page
        return redirect(url_for('home'))
    form = LoginForm()  # Create an instance of the LoginForm
    if form.validate_on_submit():  # If the form is submitted and valid
        user = User.query.filter_by(email=form.email.data).first()  # Query the user from the database
        if user and bcrypt.check_password_hash(user.password, form.password.data):  # If the user exists and the password is correct
            login_user(user, remember=form.remember.data)  # Log in the user
            next_page = request.args.get('next')  # Get the next page URL if provided
            return redirect(next_page) if next_page else redirect(url_for('home'))  # Redirect to the next page or home page
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')  # Flash a danger message
    return render_template('login.html', title='Login', form=form)  # Render the login.html template with the form

@app.route("/logout")  # Route decorator for the logout page
def logout():
    logout_user()  # Log out the current user
    return redirect(url_for('home'))  # Redirect to the home page

@app.route("/account")  # Route decorator for the account page
@login_required  # Require the user to be logged in to access this page
def account():
    return render_template('account.html', title='Account')  # Render the account.html template with the 'title' variable set to 'Account'
