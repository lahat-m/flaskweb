# Importing the Flask app object from the flaskweb module
from flaskweb import app, db
from flaskweb.models import User
# The __name__ variable is a special variable in Python that gets assigned a different value 
# depending on how the script is being executed. When the script is being run directly, 
# __name__ is set to '__main__'.
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Running the Flask app in debug mode
    app.run(debug=True)