from . import survery_bp as app
from flask import request
from flask import jsonify
from .models import Surverys
from .models import Answers

@app.route('/api/v1/survery/all')
def all_survery():
   # Obtener todas las encuestas
   surverys_db = Surverys.get_survery_all()
   
   # Crear variable de las encuestas a mostrar
   surverys = list()
   
   # Recorer lista obtenida en la base de datos
   for survery in surverys_db:
      # Estructurar datos a mostrar
      survery_dict = {
         'id': survery.id,
         'name_survery': survery.name_survery,
         'questions': survery.questions,
         'deadline': survery.deadline,
         'created_date': survery.created_date,
         'labels': survery.labels
      }

      # Guardar los datos en la lista de las encuestas
      surverys.append(survery_dict)
   return jsonify({'data': surverys})

@app.route('/api/v1/survery/one')
def one_survery():
   # obtener datos
   survery_id = request.json['survery_id']

   # Buscar encuesta
   survery_db = Surverys.get_survery_by_id(survery_id)

   # Estructurar datos de la encuesta para retornar
   survery = {
      'id': survery_db.id,
      'name_survery': survery_db.name_survery,
      'questions': survery_db.questions,
      'deadline': survery_db.deadline,
      'created_date': survery_db.created_date,
      'labels': survery_db.labels
   }

   # Buscar si existen respuestas de la encuesta
   answers_db = Answers.get_answers_of_survery(survery_db.id)

   # Lista de las respuestas a mostrar
   answers = list()
   
   if answers_db != None:
      for answer in answers_db:
         # Crear estructura a crear
         answer_dic = {
            'user': answer.user,
            'answer': survery['questions'][answer.answer],
            'answer_date': answer.answer_date
         }

         # agregar a la lista de respuestas
         answers.append(answer_dic)

   return jsonify({'survery': survery, 'answers': answers})

@app.route('/api/v1/survery/labels')
def labels_survery():
   # Obtener etiquetas
   labels = request.json['labels']

   # Obtener todas las encuestas
   surverys_db = Surverys.get_survery_all()
   
   # Crear variable de las encuestas a mostrar
   surverys = list()
   
   # Recorer lista obtenida en la base de datos
   for survery in surverys_db:
      if len(labels) == 1:
         if labels[0] in survery.labels:
            # Estructurar datos a mostrar
            survery_dict = {
               'id': survery.id,
               'name_survery': survery.name_survery,
               'questions': survery.questions,
               'deadline': survery.deadline,
               'created_date': survery.created_date,
               'labels': survery.labels
            }

            # Guardar los datos en la lista de las encuestas
            surverys.append(survery_dict)
      elif len(labels) >= 2:
         for label in  labels:
            if label in survery.labels:
               # Estructurar datos a mostrar
               survery_dict = {
                  'id': survery.id,
                  'name_survery': survery.name_survery,
                  'questions': survery.questions,
                  'deadline': survery.deadline,
                  'created_date': survery.created_date,
                  'labels': survery.labels
               }

               # Verifico que no se repita los datos
               if survery_dict not in surverys:
                  # Guardar los datos en la lista de las encuestas
                  surverys.append(survery_dict)
      else:
         # Estructurar datos a mostrar
         survery_dict = {
            'id': survery.id,
            'name_survery': survery.name_survery,
            'questions': survery.questions,
            'deadline': survery.deadline,
            'created_date': survery.created_date,
            'labels': survery.labels
         }

         # Guardar los datos en la lista de las encuestas
         surverys.append(survery_dict)

   return jsonify({'surverys': surverys})
