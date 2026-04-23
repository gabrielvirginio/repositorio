from flask import Flask, request, render_template
#pip install flask_wtf email_validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'

class RegisterForm(FlaskForm):
    first_name = StringField('Primeiro nome', validators=[DataRequired()])
    last_name = StringField('Sobrenome')
    email = StringField('E-mail', validators=[Email(message='email inválido!')])
    password = PasswordField('Senha', validators=[InputRequired(), EqualTo('confirm', message='As senhas deve ser iguais')])
    confirm = PasswordField('Confirme a senha')
    submit = SubmitField('CADASTRAR')

@app.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegisterForm()

    form.validate_on_submit()
    return render_template('register.html', form=form)

# Executando o servidor
if __name__== '__main__':
    app.run(debug=True, port=5152)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# def root():
#     return 'Olá mundo!'

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         #pegar dado form enviado via POST
#         data = request.form['name']
#         return f'Você enviou: {data}'
#     return '''
#         <form method="POST">
#             Nome: <input type="text" name="name">
#             <input type="submit" value="Enviar">
#         </form>
#     '''

# # import requests
# # response = requests.post('http://127.0.0.1:5152/submit', data={'name': 'Gabriel Virginio'})
# # print(response.text)
# @app.route('/template')
# def template():
#     return render_template('index.html', name='Dalton')