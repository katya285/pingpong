from pygame import *

window = display.set_mode((700,500))
window.fill((129,216,208))
display.set_caption('Ping-pong')

clock = time.Clock()

class GameSprite():
    def __init__(self,img,x,y,speed,w,h):
        self.image = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.w = w
        self.h = h
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
ball = GameSprite('tenis_ball.png',310,230,5,100,100)
racket1 = GameSprite('racket.png',5,200,5,40,130)
racket2 = GameSprite('racket.png',650,200,5,40,130)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.reset()
    racket1.reset()
    racket2.reset()
    display.update()
    clock.tick(60)