import os
from app import create_app, sqlAlchemy
from dotenv import load_dotenv

if __name__ == "__main__":
    # Cargar variables de entorno
    load_dotenv()

    # Configurar variables para inciar aplicacion de Flask
    app = create_app()
    host = os.environ.get('HOST', 'localhost')
    port = int(os.environ.get('PORT', 3000))
    debug = bool(os.environ.get('DEBUG', True))

    # Crear tablas
    with app.app_context():
        sqlAlchemy.create_all()

    # Iniciar aplicacion de Flask
    app.run(
        host = host,
        port = port,
        debug = debug
    )