from flask import g, Blueprint


home = Blueprint('home', __name__)


@home.route('/')
def hello_world():
  g.db.incr('visits')
  v = int(g.db.get('visits'))
  # g.db.set('visits', v + 1)
  return f'Number of visits: {v}'
