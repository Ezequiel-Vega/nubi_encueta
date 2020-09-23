from . import survery_bp as app

@app.route('/api/survery')
def survery():
   return 'Survery'