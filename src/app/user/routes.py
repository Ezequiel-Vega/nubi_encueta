from . import user_bp as app

@app.route('/api/user')
def user():
   return 'User'