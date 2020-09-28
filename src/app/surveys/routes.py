from . import survery_bp as app
from flask import request
from flask import jsonify
from .models import Surverys

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

