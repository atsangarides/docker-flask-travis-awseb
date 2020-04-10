from flask import current_app, g
from redis import Redis


def init_db():
    if 'db' not in g:
        g.db = Redis(host=current_app.config['REDIS_HOST'])
        if not g.db.exists('visits'):
            g.db.set('visits', 0)
