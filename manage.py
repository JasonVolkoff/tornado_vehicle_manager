from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado_sqlalchemy import SQLAlchemy
from settings import settings, db
from local_settings import *
from urls import url_patterns
import os



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