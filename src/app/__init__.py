import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

# Iniciar base de datos
sqlAlchemy = SQLAlchemy()

def __config(app: Flask):
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secretkey')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'jwtsecretkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URI',
        'sqlite:////tmp/test.db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

def __routes(app: Flask):
    from .admin import admin_bp
    from .auth import auth_bp
    from .history import history_bp
    from .surveys import survery_bp
    from .user import user_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(survery_bp)
    app.register_blueprint(user_bp)

def create_app() -> Flask:
    # Inctanciar objetos
    _app = Flask(__name__)

    # Llamar a las configuraciones
    __config(_app)
    
    # Iniciar CORS
    _cors = CORS(_app, resources={r"/api/*": {"origins": "*"}})
    
    # Iniciar JWT
    _jwt = JWTManager(_app)
    
    # Crear tablas
    sqlAlchemy.init_app(_app)
    
    # Llamar a las rutas
    __routes(_app)

    # Retornar app de flask
    return _app