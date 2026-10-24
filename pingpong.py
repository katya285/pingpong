from pygame import *

window = display.set_mode((700,500))
window.fill((129,216,208))
display.set_caption('Ping-pong')
font.init()
win1 = font.SysFont('verdana',40).render('Выиграл игрок 1', True,(255,255,255))
win2 = font.SysFont('verdana',40).render('Выиграл игрок 2', True,(255,255,255))


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

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y> 0:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y<370:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.y> 0:
            self.rect.y -= self.speed
        elif keys[K_c] and self.rect.y<370:
            self.rect.y += self.speed

ball = GameSprite('tenis_ball.png',310,230,5,70,70)
racket1 = Player1('racket.png',5,200,5,40,130)
racket2 = Player2('racket.png',650,200,5,40,130)
game = True
speed_x = 3
speed_y = 3
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((129,216,208))
        ball.rect.x +=speed_x
        ball.rect.y +=speed_y

        if sprite.collide_rect(ball,racket1) or sprite.collide_rect(ball,racket2):
            speed_x *= -1
        if ball.rect.y<0 or ball.rect.y >430:
            speed_y *= -1
        if ball.rect.x <0:
            window.blit(win1,(200,200))
            finish = True
        if ball.rect.x >630:
            window.blit(win2,(200,200))
            finish = True

        ball.reset()
        racket1.reset()
        racket2.reset()
        racket1.update()
        racket2.update()
    display.update()
    clock.tick(60)