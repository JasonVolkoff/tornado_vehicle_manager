import os
from local_settings import DEBUG
from tornado_sqlalchemy import SQLAlchemy
from local_settings import database_url

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'debug': DEBUG
}

db=SQLAlchemy(database_url)
target_metadata = db.metadata