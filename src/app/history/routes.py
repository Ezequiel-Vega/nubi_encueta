from . import history_bp as app

@app.route('/api/history')
def history():
   return 'History'