from pygame import *
'''Необходимые классы'''
 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed,player_width, player_hight):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image),(player_hight,player_width))
       
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed 
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class PlayerSprite(GameSprite):
    def updata(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 250: 
           self.rect.y += self.speed
    def updata1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 250: 
           self.rect.y += self.speed

#Игровая сцена:
back = (200,255,255)
win_width = 900
win_height =800
window = display.set_mode((win_width, win_height))
window.fill(back)
 
#Персонажи игры:
player1 = PlayerSprite('racket.png', 10, 400, 4,250,100)
player2 = PlayerSprite('racket.png', 800, 300, 4,250,100)
ball = GameSprite ('tenis_ball.png', 400, 400, 3, 100 ,150)



game = True
Finish = False
Super = False
clock = time.Clock()
FPS = 60


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        
    window.fill(back)
    player1.reset()
    player2.reset()
    player1.updata()
    player2.updata1()
    ball.reset()
    display.update()
    clock.tick(FPS)           