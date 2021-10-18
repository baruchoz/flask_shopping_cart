from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'randomstuff'


from app import routes