from leancloud import Engine
from bot import bot

engin = Engine(bot)

@engin.define
def hell(**parms):
    if 'name' in parms:
        return 'hello ,{}!'.format(parms['name'])
    else:
        return 'hello leancloud'