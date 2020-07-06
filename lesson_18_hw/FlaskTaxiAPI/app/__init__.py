"""Создание экземпляра класса приложения."""
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///onyx_taxi.db'

from app import views
