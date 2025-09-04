import dj_database_url
import os
from dotenv import load_dotenv

from .base import *

# load dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))

SECRET_TOKEN_KEY = os.getenv("PRODUCTION_SECRET_TOKEN_KEY")
SECRET_TOKEN_ALGO = os.getenv("PRODUCTION_SECRET_TOKEN_ALGO")

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("PRODUCTION_DATABASE_URL"),
        conn_max_age=None # keeps single connection for all quires + transactions session
    )
}