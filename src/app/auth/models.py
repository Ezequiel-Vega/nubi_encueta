import datetime
from app import bcrypt
from app import sqlAlchemy as db

class User(db.Model):

    # Declarar el nombre de la tabla
    __tablename__ = 'users'

    # Declarar los parametros
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = True)
    password = db.Column(db.String(150), nullable = False)
    is_admin = db.Column(db.Boolean, default = False)

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'

    def encrypt_password(self, password: str):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str):
        return bcrypt.check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Metodos para obtener un User
    @staticmethod
    def get_by_id(id: int):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email: str):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_all():
        return User.query.all()