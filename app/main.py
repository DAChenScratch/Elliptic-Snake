import bottle
import os
import random
from app.game import Game
from app.taunts import taunts


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#FF0AD2',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'Elliptic Snake',
        'head_type': 'safe',
        'tail_type': 'curled'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    game1 = Game(data['height'],data['width'],data['game_id'])
    game1.parse_data(data)
    move = game1.move()

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']
    
    taunt = taunts(game1.snakes[0]["health_points"])

    return {
        'move': move,
        'taunt': taunt
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
