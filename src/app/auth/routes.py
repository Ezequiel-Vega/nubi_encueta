from . import auth_bp as app

@app.route('/api/auth')
def auth():
   return 'Auth'