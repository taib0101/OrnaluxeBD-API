import dj_database_url
import os
from dotenv import load_dotenv

from .base import *

# load dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))

SECRET_TOKEN_KEY = os.getenv("DEVELOPMENT_SECRET_TOKEN_KEY")
SECRET_TOKEN_ALGO = os.getenv("DEVELOPMENT_SECRET_TOKEN_ALGO")

HOST = os.getenv("DEVELOPMENT_HOST")
BIND_PORT = int(os.getenv("DEVELOPMENT_BIND_PORT"))

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DEVELOPMENT_DATABASE_URL"), # local host: postgres://root:1234@localhost:5432/mydatabase
        conn_max_age=None # keeps single connection for all quires + transactions session
    )
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True