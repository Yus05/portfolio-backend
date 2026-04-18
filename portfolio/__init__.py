import os 
from flask import Flask, render_template


def create_app():
    
    app = Flask(__name__)
    
    secret_key = os.environ.get('SECRET_KEY')
    
    if not secret_key and not app.debug:
        raise ValueError("No se ha configurado la variable de entorno SECRET_KEY")
    
    app.config.from_mapping(
        SECRET_KEY = secret_key
    )
    
    # Registro de Blueprints
    from . import views
    app.register_blueprint(views.bp)
    
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app