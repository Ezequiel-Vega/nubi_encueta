import datetime
from . import user_bp as app
from flask import request
from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import jwt_optional
from flask_jwt_extended import get_jwt_identity
from .models import User
from app.surveys.models import Surverys
from app.surveys.models import Answers

@app.route('/api/v1/user/add', methods=['POST'])
@jwt_required
def add_survery():
   # Obtener datos
   name_survery = request.json['name_survery']
   questions = request.json['questions']
   answers_correct = request.json['correct_answers']
   deadline = datetime.datetime.strptime(
      request.json['deadline'],
      "%d/%m/%Y"
   )
   labels = request.json['labels']
   id_user = get_jwt_identity()

   if len(questions) <= 4:
      # Crear modelo a guardar
      survery = Surverys(
         name_survery,
         questions,
         answers_correct,
         deadline,
         labels,
         id_user
      )

      # Guardar encuesta
      save_survery = survery.save()

      return jsonify({'error': False, 'msg': save_survery})
   else:
      return jsonify({'error': True, 'msg': 'No se pude guardar mas de 4 preguntas'})

@app.route('/api/v1/user/answer', methods=['POST'])
@jwt_optional
def answer_surverys():
   # Obtener resultados
   user_id = get_jwt_identity()
   if user_id != None:
      get_user = User.get_by_id(user_id)
      user = get_user.username
   else:
      user = 'Anonymous'

   answers = request.json['answers']
   answer_date = datetime.datetime.now()
   survery_id = request.json['survery_id']

   for answer in answers:
      # Crear modelo a guardar
      model_answer = Answers(
         user,
         answer_date,
         answer,
         survery_id
      )

      # guardar datos
      save_answer = model_answer.save()

   return jsonify(save_answer)