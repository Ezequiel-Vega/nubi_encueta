from . import admin_bp as app

@app.route('/api/admin')
def admin():
   return 'Admin'