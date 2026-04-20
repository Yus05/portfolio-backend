import os 
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect

from .forms import ContactForm

mail = Mail()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    
    secret_key = os.environ.get('SECRET_KEY')
    
    if not secret_key and not app.debug:
        raise ValueError("No se ha configurado la variable de entorno SECRET_KEY")
    
    app.config.from_mapping(
        SECRET_KEY = secret_key, 
        
        # Configuracion de Flask Mail
        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT = 587,
        MAIL_USE_TLS = True,
        MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
        MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    )
    
    mail.init_app(app)
    csrf.init_app(app)
    
    
    # Registro de Blueprints
    from . import views
    app.register_blueprint(views.bp)
    
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = ContactForm()
        
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            message_body = form.message.data
            
            msg = Message(subject=f"NUEVO MENSAJE PORTFOLIO: {name}",
                          sender=app.config['MAIL_USERNAME'],
                          recipients=['ysomaza@gmail.com'])
            
            msg.body = f"""
            Has recibido un nuevo mensaje de contacto:
            Nombre: {name}
            Correo de contacto: {email}
            Mensaje:
            {message_body}
            """
            
            try:
                mail.send(msg)
                flash('¡Gracias por contactarnos! Tu mensaje ha sido enviado con éxito.', 'success')
            except Exception as e:
                flash(f'Ocurrió un error al enviar el mensaje: {str(e)}', 'danger')
            
            return redirect(url_for('index'))
        
        return render_template('index.html', form=form)
    
    return app