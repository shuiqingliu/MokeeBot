from leancloud import Engine
from app import app

engin = Engine(app)

@engin.define
def hell(**parms):
    if 'name' in parms:
        return 'hello ,{}!'.format(parms['name'])
    else:
        return 'hello leancloud'