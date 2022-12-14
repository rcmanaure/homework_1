import uuid
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from flask_login import LoginManager
from flasgger import Swagger
from sqlalchemy.dialects.postgresql import UUID
from services.config.swagger import template, swagger_config

# Init Flask.
app = Flask(__name__)
app_test = app

#  Config Variables to be used for Flask.
app.config.from_object("config.Config")

# Init SQLAlchemy so we can use it later in our models
db = SQLAlchemy(app)
db.init_app(app)

# Flask-Login config.
# https://flask-login.readthedocs.io/en/latest/
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

# Init Swagger
Swagger(app, config=swagger_config, template=template)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in
    #  the query for the user
    return User.query.get(int(user_id))


class User(
    db.Model,
    UserMixin,
):
    # Model User to be created in Postgresql.

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(100), nullable=True, default="default.png")
    password = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    create_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Item(db.Model):
    # Model Post to be created in Postgresql.(Publicacion)

    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), default="WAITING", nullable=True)
    capacity = db.Column(db.Integer, default=100, nullable=False)
    package = db.Column(db.String(30), nullable=True)
    fridge = db.Column(db.Boolean, nullable=True)
    user_id = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(100), nullable=False)

    create_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}')"
