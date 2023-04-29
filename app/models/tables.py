from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True,  nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100))
    

    def __init__(self, password, name, email):
        self.name = name
        self.email = email
        self.senha = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(password)


    def __repr__(self):
        return "<User %r>" % self.username
db.create_all()
