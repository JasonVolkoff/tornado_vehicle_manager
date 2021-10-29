from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado_sqlalchemy import SQLAlchemy
from settings import *
from urls import url_patterns
import os

# Create a local_settings file; it must contain the following:
"""
DEBUG = True
DEVELOPMENT = True
database_url = "postgresql://YOUR_USERNAME:YOUR_PASSWORD@localhost:YOUR_PORT/YOUR_DATABASE_NAME"
"""
# This example `database_url` uses postgreSQL, feel free to use w/e you want (SQL, SQLite, etc)

try:
    from local_settings import *
except ImportError:
    pass

class TornadoVehicle(Application):
    def __init__(self):
        Application.__init__(self, url_patterns, **settings, db=db)

def main():
    app = TornadoVehicle()
    port = int(os.environ.get("PORT", 5000))
    print(f"Lisetning on port: {port}")
    app.listen(port)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()