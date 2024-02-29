import pygame
import pygame_menu
from pygame_menu import themes
import random

pygame.init()
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Сапёр")
pygame.mixer.music.load("data/fon_menu.mp3")
pygame.mixer.music.play(-1)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
size = width, height = 600, 400


class Ball(pygame.sprite.Sprite):  # с этого момента до функции set_difficulty - шары для фона
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("blue"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 1)
        self.vy = random.randrange(-1, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


Border(0, 0, width - 0, 0)
Border(0, height - 0, width - 0, height - 0)
Border(0, 0, 0, height - 0)
Border(width - 0, 0, width - 0, height - 0)

for i in range(13):
    Ball(2, 350, 200)


def set_difficulty(value, difficulty):  # сдесь начинаются функции
    print(value)  # связанные с меню игры
    print(difficulty)


def start_the_game():
    from main import new_game
    mainmenu._open(new_game)


def level_menu():
    mainmenu._open(level)


def pravila_menu():
    mainmenu._open(pravila)


mainmenu = pygame_menu.Menu('САПЁР', 600, 400, theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Введите никнейм: ', default='unknown')
mainmenu.add.button('Играть', start_the_game)
mainmenu.add.button('Уровни', level_menu)
mainmenu.add.button('Об игре и её правилах', pravila_menu)
mainmenu.add.button('Выход из игры', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Все уровни генерируются', 600, 400, theme=themes.THEME_BLUE)
level.add.selector('Сложность :', [('Как повезёт', 1), ('Как повезёт', 1)], onchange=set_difficulty)

pravila = pygame_menu.Menu('Об игре и её правилах', 600, 400, theme=themes.THEME_BLUE)
pravila.add.text_input("можете прочитать, введя ссылку в Гугл:")
pravila.add.text_input("https://ru.wikipedia.org/wiki/Сапёр_(игра)")

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(window)
    all_sprites.draw(window)
    all_sprites.update()
    pygame.display.update()