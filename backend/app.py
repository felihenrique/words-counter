from flask import Flask
from application.modules.words.controller import bp as words_bp
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.register_blueprint(words_bp)
