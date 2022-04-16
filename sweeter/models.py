from flask_login import UserMixin

from sweeter import db, manager

class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.Strung(128), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)

@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
