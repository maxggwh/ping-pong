from pygame import *
from random import *
window = display.set_mode((700, 500))
display.set_caption('raw1/ping-pong')
background = transform.scale(image.load('images (7).jpg'), (700, 500))
font.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
          keys_pressed = key.get_pressed()
          if keys_pressed[K_UP]and self.rect.y > 5:
            self.rect.y -= self.speed
          if keys_pressed[K_DOWN] and self.rect.y < 458:
            self.rect.y += self.speed
    def update2(self):
          keys_pressed = key.get_pressed()
          if keys_pressed[K_w]and self.rect.y > 5:
            self.rect.y -= self.speed
          if keys_pressed[K_s] and self.rect.y < 458:
            self.rect.y += self.speed
player = Player('racket.png', 20, 200, 10, 40, 10)
player2 = Player('racket.png', 680, 200, 10, 40, 10)
mcha = GameSprite('ball.png', 340, 250, 50, 50, 0)
clock = time.Clock()
FPS=60
game = True
speed_x = 3
speed_y = 3
finish = False
font1 = font.Font(None, 35)
lose1=font1.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2=font1.render('PLAYER 2 LOSE', True, (180, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        mcha.rect.x += speed_x
        mcha.rect.y += speed_y
        window.blit(background,(0, 0))
        if mcha.rect.y > 450 or mcha.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player, mcha) or sprite.collide_rect(player2, mcha):
            speed_x *= -1
        if mcha.rect.x <0:
            finish=True
            window.blit(lose1,(200,200))
        if mcha.rect.x >700:
            finish=True
            window.blit(lose2,(200,200))
       
        player.update()
        player2.update2()
        player2.reset()
        player.reset()
        mcha.reset()
            
                    
        clock.tick(FPS)
        display.update()
display.update()
