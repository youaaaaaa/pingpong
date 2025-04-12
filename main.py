#Создай собственный Шутер!

from pygame import *
from pygame import sprite
from random import randint
from time import time as timer

window_size_x = 700
window_size_y = 500
player_size_x = 50
player_size_y = 100
score = 0 # сбито
lost = 0 # пропущено
bullets = sprite.Group()


class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
     
    def goLeft(self):
        if self.rect.x >= self.speed:
            self.rect.x -= self.speed

    def goRight(self):
        if self.rect.x < window_size_x - self.size_x and self.rect.x < window_size_x - self.speed:
            self.rect.x += self.speed

    def goUp(self):
        if self.rect.y >= self.speed:
            self.rect.y -= self.speed

    def goDown(self):
        if self.rect.y < window_size_y - self.size_y and self.rect.y < window_size_y - self.speed:
            self.rect.y += self.speed


class Player (GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            super().goUp()
        if keys_pressed[K_DOWN]:
            super().goDown()
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            super().goUp()
        if keys_pressed[K_s]:
            super().goDown()
      

class Ball(GameSprite):
    #надо обработать движение на вектор (dx, dy) и столкновение со стенками
    def goThere(self, dx,dy):
        if dy==0:
            dy=1
        if self.rect.x >= self.speed and self.rect.x < window_size_x - self.size_x and self.rect.x < window_size_x - self.speed:
            self.rect.x += dx*self.speed
        if self.rect.y >= self.speed and self.rect.y < window_size_y - self.size_y and self.rect.y < window_size_y - self.speed:
            self.rect.y += dy*self.speed



window = display.set_mode((700,500))

display.set_caption("PingPong")

background = transform.scale(image.load("table.jpg"),(700,500))

FPS = 60
clock = time.Clock()
game=True

mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()

font.init()
font2 = font.SysFont('Arial', 36)
font1 = font.SysFont('Arial', 72)


player_left = Player("puddle.jpg",10, 250, 25, 100, 10)
player_right = Player("puddle.jpg",670, 250, 25, 100, 10)


finish=False

while game:

    for e in event.get():
        if e.type==QUIT:
            game=False

    if not finish:
        window.blit(background,(0,0))
        player_left.update_l()
        player_right.update_r()

        player_left.reset()
        player_right.reset()
    
    display.update()

    time.delay(50)
    
    clock.tick(FPS)
