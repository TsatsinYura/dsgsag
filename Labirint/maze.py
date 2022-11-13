from pygame import *
'''Шрифт'''
font.init()
font = font.SysFont('Times New Roman',50)
win = font.render('YOU WIN!',True, (237, 0, 8))
lose = font.render('YOU LOSE!',True, (237, 0, 8))
'''Переменные для картинок'''
img_back = 'galaxy.jpg'
img_hero = 'cyborg.png'
img_enemy = 'скелет.png'
'''Классы'''
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Wall(sprite.Sprite):
    def __init__(self, red, green, blue, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue
        self.w = wall_width
        self.h = wall_height
        # каждый спрайт должен хранить свойство image - изображение
        self.image = Surface((self.w, self.h))
        self.image.fill((red,green,blue))
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
'''Окно игры'''
#Создаём окошко
win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load(img_back),(win_width,win_height))
'''Персонажи'''
hero = Player(img_hero, 5, win_height - 80, 65,65,10)
monster = GameSprite(img_enemy, 100,400,65,65,10)
'''Стены'''
w1 = Wall(127, 74, 169,180, 200, 400, 10)
w2 = Wall(127, 74, 169,100, 50, 10, 100)
w3 = Wall(127, 74, 169,350, 100, 40, 120)
w4 = Wall(127, 74, 169,180, 200, 250, 100)
'''Игровой цикл'''
game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(back, (0,0))
        hero.reset()
        monster.reset()
        hero.update()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        if sprite.collide_rect(hero, monster):
            finish = True
            window.blit(lose,(200,200))
    display.update()
    clock.tick(FPS)