import json
from . import auth_bp as app
from flask import request
from flask import jsonify
from flask_jwt_extended import create_access_token
from .models import User

@app.route('/api/v1/auth/sign_up', methods=['POST'])
def sign_up():
   # Obtener datos
   username = request.json['username']
   email = request.json['email']
   password = request.json['password']
   confirm_password = request.json['confirm_password']

   # Comprobar si existe un usuario ya registrado
   user = User.get_by_email(email)

   if user is not None:
      response = {
         'error': True,
         'msg': 'Upss! Este email ya esta registrado con un usuario!'
      }
      return jsonify(response)
   elif password == confirm_password: # Comprobar si las contraseñeas coinciden
      # Crear modelo de usuario para guardar
      user = User(
         username = username,
         email = email
      )
      
      # Encriptar password
      user.encrypt_password(password)
      
      # Guardar usuario
      user.save()
      
      # retornar respuesta
      response = {
         'error': False,
         'msg': 'Usuario registrado exitosamente!'
      }
      return jsonify(response)
   else:
      response = {
         'error': True,
         'msg': 'Upss! Las contraseñeas no coinciden!'
      }
      return jsonify(response)

@app.route('/api/v1/auth/sign_in', methods=['POST'])
def sign_in():
   # Obtener datos
   email = request.json['email']
   password = request.json['password']

   # Buscar usuario
   user = User.get_by_email(email)

   if user is not None:
      if user.check_password(password):
         # Crear Token
         token = create_access_token(identity=user.id)

         # Crear respuesta
         response = {
            'error': False,
            'token': token,
            'msg': 'Sign in Exitoso!'
         }
         return jsonify(response)
      else:
         # Crear respuesta
         response = {
            'error': True,
            'token': '',
            'msg': 'Upss! Contraseñea invalida!'
         }
         return jsonify(response)
   else:
      # Crear respuesta
      response = {
         'error': True,
         'token': '',
         'msg': 'Upss! El usuario no esta registrado!'
      }
      return jsonify(response)