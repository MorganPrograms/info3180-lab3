from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'passphare'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'b178eec033aa52'
app.config['MAIL_PASSWORD'] = '58b8e5d76788e3'
mail = Mail(app)
from app import views
