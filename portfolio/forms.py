from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[
        DataRequired(message="Por favor, ingresa tu nombre.")
    ])
    
    email = StringField('Correo Electronico', validators=[
        DataRequired(message="El correo es obligatorio."),
        Email(message="Ingresa un correo electronico valido.")
    ])
    
    message = TextAreaField('Mensaje', validators=[
        DataRequired(message="El mensaje no puede estar vacío."),
        Length(min=10, message="Cuéntanos un poco más (mínimo 10 caracteres).")
    ])
    
    submit = SubmitField('Enviar Mensaje')