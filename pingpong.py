from pygame import *

window = display.set_mode((700,500))
window.fill((129,216,208))
display.set_caption('Ping-pong')

clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)