from flask import Flask, render_template

def create_app():
    
    app = Flask(__name__)
    
    # Configuracion del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev'
    )
    
    # Registro de Blueprints
    from . import views
    app.register_blueprint(views.bp)
    
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app