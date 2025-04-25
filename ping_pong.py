from pygame import *
from random import *
window = display.set_mode((700, 500))
display.set_caption('raw1/ping-pong')
background = transform.scale(image.load('images (7).jpg'), (700, 500))

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
          if keys_pressed[K_LEFT]and self.rect.x > 5:
            self.rect.x -= speed
          if keys_pressed[K_RIGHT] and self.rect.x < 625:
            self.rect.x += speed
        player = Player('racket.png', 100, 200, 65, 65, 30)
clock = time.Clock()
FPS=60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0, 0))
        
                
    clock.tick(FPS)
    display.update()