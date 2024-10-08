"""Connect Four

Exercises

1. Change the colors.
2. Draw squares instead of circles for open spaces.
3. Add logic to detect a full row.
4. Create a random computer player.
5. How would you detect a winner?
"""

import turtle

from freegames import line

turns = {'red': 'yellow', 'yellow': 'red'}
state = {'player': 'yellow', 'rows': [0] * 8}


def grid():
    """Draw Connect Four grid."""
    turtle.bgcolor('light blue')

    for x in range(-150, 200, 50):
        line(x, -200, x, 200)

    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            turtle.up()
            turtle.goto(x, y)
            turtle.dot(40, 'white')

    turtle.update()


def tap(x, y):
    """Draw red or yellow circle in tapped row."""
    player = state['player']
    rows = state['rows']

    row = int((x + 200) // 50)
    count = rows[row]

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    turtle.up()
    turtle.goto(x, y)
    turtle.dot(40, player)
    turtle.update()

    rows[row] = count + 1
    state['player'] = turns[player]


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.onscreenclick(tap)
turtle.done()
