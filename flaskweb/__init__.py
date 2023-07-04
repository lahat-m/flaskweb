# Importing necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Creating a Flask application instance
app = Flask(__name__)

# Configuring the application
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'  # Secret key for secure sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database URI
# Note: Here 'site.db' is the name of the SQLite database file. You can change it as per your requirement.

# Initializing the SQLAlchemy database
db = SQLAlchemy(app)

# Initializing the Bcrypt password hashing utility
bcrypt = Bcrypt(app)

# Initializing the LoginManager
login_manager = LoginManager(app)

# Setting the login view for the LoginManager
login_manager.login_view = 'login'
# Note: 'login' is the name of the view function or route where users are redirected for logging in.

# Setting the category for login messages
login_manager.login_message_category = 'info'
# Note: 'info' is the category used for displaying login-related messages.

# Importing routes from the flaskweb module
from flaskweb import routes
