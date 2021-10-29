from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin, as_future
from .models.user import User

class HomeHandler(SessionMixin, RequestHandler):
    async def get(self):
        with self.make_session() as session:
            count = await as_future(session.query(User).count)

        self.write('{} users so far!'.format(count))