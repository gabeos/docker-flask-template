# coding:utf-8

from app.app import create_app
from app.settings import Config

app = create_app(Config)
