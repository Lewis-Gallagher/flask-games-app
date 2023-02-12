import os
import secrets

class Config(object):
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_urlsafe(16)