from flask import Flask
from config import Config
from .routes import site

app = Flask(__name__)

app.register_blueprint(site)

app.config.from_object(Config)





