import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()
pygame.mixer.music.load("data/fon_music.mp3")
pygame.mixer.music.play(-1)


def new_game(count_bombs):  # создание новой игры
    free_field = [[x, y] for y in range(0, 16) for x in range(0, 8)]  # список свободных полей
    coordinat = []  # список для координат бомб
    for x in range(count_bombs):  # заполняем список бомбами
        rand_element = random.choice(free_field)
        coordinat.append(rand_element)
        free_field.remove(rand_element)
    count_bombs = bombs
    massive = [[0 for i in range(stolb)] for j in range(stroki)]  # матрица для хранения координат бомб
    massive_kletki = [[0 for i in range(stolb)] for j in
                      range(stroki)]  # матрица для хранения информации о закрытых или открытых клетках
    massive_test = [[0 for i in range(stolb)] for j in
                    range(stroki)]  # матрица для хранения информации о клетках неприлегающих к бомбам
    timer = False  # запустить или не запустить часы
    finded = False
    second = "000"  # начальное значение часов
    for y in coordinat:  # заполняем массив бомбами из списка coordinat
        massive[int(y[0])][int(y[1])] = 9

    for i in range(stroki):  # расставление цифр вокруг бомб
        for j in range(stolb):
            if massive[i][j] == 0:
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < stroki and 0 <= y < stolb and massive[x][y] == 9:
                            massive[i][j] += 1
    for y in range(16):  # связываем цифру с графическим файлом
        for x in range(16):
            if massive[y][x] == 0:
                picture = "data/d0.png"
            elif massive[y][x] == 1:
                picture = "data/d1.png"
            elif massive[y][x] == 2:
                picture = "data/d2.png"
            elif massive[y][x] == 3:
                picture = "data/d3.png"
            elif massive[y][x] == 4:
                picture = "data/d4.png"
            elif massive[y][x] == 5:
                picture = "data/d5.png"
            elif massive[y][x] == 6:
                picture = "data/d6.png"
            elif massive[y][x] == 7:
                picture = "data/d7.png"
            elif massive[y][x] == 8:
                picture = "data/d8.png"
            elif massive[y][x] == 9:
                picture = "data/bomb1.png"
            gr_sign.add(Sign((x * 35 + 23, y * 35 + 120), picture))
    for y in range(16):  # заполняем пустыми клетками группу
        for x in range(16):
            gr_kletka.add(Kletka((x * 35 + 23, y * 35 + 120), "data/kletka1.png", 0))
    btn1.win = 1  # win=0(проигрыш),win=1(идёт игра),win=2(выигрыш)
    return massive_kletki, massive, massive_test, count_bombs, timer, second


class Kletka(pygame.sprite.Sprite):  # спрайты, покрывающие поле поверх цифр
    def __init__(self, coord, picture, state):
        super().__init__()
        self.image = pygame.image.load(picture).convert()
        self.rect = self.image.get_rect(topleft=coord)
        self.state = state


class Sign(pygame.sprite.Sprite):  # спрайты цифр и бомб
    def __init__(self, coord, picture):
        super().__init__()
        self.image = pygame.image.load(picture).convert()
        self.rect = self.image.get_rect(topleft=coord)


class Knop(pygame.sprite.Sprite):  # кнопка со смайлом
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/btn1.png").convert()
        self.rect = self.image.get_rect(center=(300, 60))
        self.state = 0
        self.win = 1  # состояние игры 0=проигрыш, 1=играем, 2=выигрыш


class Digit(pygame.sprite.Sprite):  # спрайты для выведения цифр на счётчиках
    def __init__(self, x, y):
        super().__init__()
        self.long_image = pygame.image.load("data/Digit1.png").convert()
        self.image = pygame.Surface((28, 50))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update_digit(self, number):  # вырезания определённой цифры из большого файла
        if number == "0":
            self.image.blit(self.long_image, (0, 0), (28, 0, 28, 50))
        elif number == "1":
            self.image.blit(self.long_image, (0, 0), (56, 0, 28, 50))
        elif number == "2":
            self.image.blit(self.long_image, (0, 0), (84, 0, 28, 50))
        elif number == "3":
            self.image.blit(self.long_image, (0, 0), (112, 0, 28, 50))
        elif number == "4":
            self.image.blit(self.long_image, (0, 0), (140, 0, 28, 50))
        elif number == "5":
            self.image.blit(self.long_image, (0, 0), (168, 0, 28, 50))
        elif number == "6":
            self.image.blit(self.long_image, (0, 0), (196, 0, 28, 50))
        elif number == "7":
            self.image.blit(self.long_image, (0, 0), (224, 0, 28, 50))
        elif number == "8":
            self.image.blit(self.long_image, (0, 0), (252, 0, 28, 50))
        elif number == "9":
            self.image.blit(self.long_image, (0, 0), (280, 0, 28, 50))
        elif number == "-":
            self.image.blit(self.long_image, (0, 0), (0, 0, 28, 50))


# начало программы
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Сапёр")
gr_kletka = pygame.sprite.Group()  # создаём группу класса Kletka(квадраты закрывающие цифры)
gr_sign = pygame.sprite.Group()  # создаём группу класса Sign(изображения цифр и бомб)
background = pygame.image.load("data/pole1.png").convert()  # изображение бекграунда
btn1 = Knop()  # создаём кнопку смайл
stroki = 16  # кол-во строк, столбцов и бомб
stolb = 16
bombs = 20

count_bombs = bombs
str_bomb = str(bombs).zfill(3)  # добавляем к строке недостающие нули
press = False  # переменная для опредения нажатия левой кнопки
timer = False  # запустить или не запустить часы
second = "000"
close_kletka = 256  # кол-во закрытых клеток(для создания списка новых бомб)
digit_1 = Digit(33, 34)  # создания объектов для вывода цифр в счётчиках
digit_2 = Digit(61, 34)
digit_3 = Digit(89, 34)
clock1 = Digit(490, 34)
clock2 = Digit(518, 34)
clock3 = Digit(546, 34)
massive_kletki, massive, massive_test, count_bombs, timer, second = new_game(count_bombs)  # запуск новой игры
while True:
    for ev in pygame.event.get():  # перехват событий
        if ev.type == pygame.QUIT:  # если нажали на закрытие окна
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEMOTION:  # если двигаем мышку
            if btn1.state == 1 and not (btn1.rect.collidepoint(
                    pygame.mouse.get_pos())) and btn1.win == 1:  # если идёт игра, курсор не попал на кнопку смайл и она была нажата
                btn1.state = 0  # седлать кнопку смайл ненажатой
                btn1.image = pygame.image.load("data/btn1.png").convert()  # поменять на ней картинку
            elif btn1.state == 1 and not (btn1.rect.collidepoint(
                    pygame.mouse.get_pos())) and btn1.win == 2 and press == True:  # она была нажата, курсор не попал на кнопку смайл, мы выиграли, левая кнопка мыши нажата
                btn1.state = 3  # поменять на смайл в очках
                btn1.image = pygame.image.load("data/btn5.png").convert()
            elif btn1.state == 1 and not (btn1.rect.collidepoint(
                    pygame.mouse.get_pos())) and btn1.win == 0:  # она нажата, курсор не попал на кнопку смайл и мы проиграли
                btn1.state = 2  # поменять на смайл с крестиками
                btn1.image = pygame.image.load("data/btn3.png").convert()
            elif btn1.state == 2 and btn1.rect.collidepoint(
                    pygame.mouse.get_pos()) and btn1.win == 0 and press == True:  # если он с крестиками, курсор попал на кнопку смайл, мы проиграли, левая кнопка нажата
                btn1.state = 1  # меням на нажатый смайл
                btn1.image = pygame.image.load("data/btn4.png").convert()
            elif btn1.state == 3 and btn1.rect.collidepoint(
                    pygame.mouse.get_pos()) and btn1.win == 2 and press == True:  # если смайл с очками, курсор попал на кнопку, мы выиграли, левая кнопка нажата
                btn1.state = 1  # меняем на нажатый смайл
                btn1.image = pygame.image.load("data/btn4.png").convert()

        if ev.type == pygame.MOUSEBUTTONUP:
            press = False
            if ev.button == pygame.BUTTON_LEFT:  # отжатие левой кнопки
                if btn1.rect.collidepoint(pygame.mouse.get_pos()):  # если нажали по кнопке со смайлом и отжали
                    if btn1.state == 1:
                        massive_kletki, massive, massive_test, count_bombs, timer, second = new_game(
                            count_bombs)  # начать новую игру
                    btn1.state = 0  # кнопка со смайлом
                    btn1.image = pygame.image.load("data/btn1.png").convert()
            if btn1.state == 1 and btn1.rect.collidepoint(
                    pygame.mouse.get_pos()) and btn1.win == 0:  # если она нажата, курсор на кнопке и мы проиграли
                btn1.state = 0
                btn1.image = pygame.image.load("data/btn1.png").convert()
                massive_kletki, massive, massive_test, count_bombs, timer, second = new_game(
                    count_bombs)  # начать новую игру

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == pygame.BUTTON_RIGHT:
                r_klik = pygame.mixer.Sound("data/klik.ogg")
                r_klik.play()
                if btn1.win == 1 and 23 < pygame.mouse.get_pos()[0] < 583 and 120 < pygame.mouse.get_pos()[1] < 680:
                    # если идёт игра, кликнули по клетке
                    coord = (pygame.mouse.get_pos()[1] - 120) // 35, (
                            pygame.mouse.get_pos()[0] - 23) // 35  # ловим координаты нажатия
                    if massive_kletki[(pygame.mouse.get_pos()[1] - 120) // 35][
                        (pygame.mouse.get_pos()[0] - 23) // 35] == 0:  # если она закрыта
                        for kl in gr_kletka:  # уничтожаем серую клетку, ставим новую с флагом или вопросом
                            if kl.rect.collidepoint(pygame.mouse.get_pos()):
                                state = kl.state
                                kl.kill()
                        if state == 0:  # если кнопка обычная
                            gr_kletka.add(
                                Kletka((coord[1] * 35 + 23, coord[0] * 35 + 120), "data/flag.png", 1))  # ставим флаг
                            count_bombs -= 1  # убовляем счётчик бомб
                        elif state == 1:  # если кнопка с флагом
                            gr_kletka.add(
                                Kletka((coord[1] * 35 + 23, coord[0] * 35 + 120), "data/quest.png", 2))  # ставим вопрос
                            count_bombs += 1  # прибавляем кол-во бомб
                        elif state == 2:  # если кнопка с вопросом
                            gr_kletka.add(Kletka((coord[1] * 35 + 23, coord[0] * 35 + 120), "data/kletka1.png",
                                                 0))  # ставим обычную клетку
            if ev.button == pygame.BUTTON_LEFT:  # нажатие левой кнопки мыши
                l_klik = pygame.mixer.Sound("data/klik.ogg")
                l_klik.play()
                press = True  # запомнить что кнопка нажата
                if btn1.win == 1:  # если идёт игра
                    if btn1.rect.collidepoint(pygame.mouse.get_pos()):  # если попали по большой кнопке
                        btn1.image = pygame.image.load("data/btn4.png").convert()
                        btn1.state = 1  # меняем на нажатую кнопку
                    for kl in gr_kletka:
                        if kl.rect.collidepoint(pygame.mouse.get_pos()):  # если попали по клетке
                            if timer == False:  # если таймер не идёт
                                start = pygame.time.get_ticks()  # запускаем таймер
                            timer = True  # запоминаем состояние таймера
                            if kl.state == 0:  # если клетка серая
                                massive_kletki[(pygame.mouse.get_pos()[1] - 120) // 35][
                                    (pygame.mouse.get_pos()[0] - 23) // 35] = 1  # говорим, что она открыта
                                if massive[(pygame.mouse.get_pos()[1] - 120) // 35][(pygame.mouse.get_pos()[0] - 23) // 35] == 0:
                                # если стоит ноль, открываем соседние поля
                                    coord = (pygame.mouse.get_pos()[1] - 120) // 35, (
                                            pygame.mouse.get_pos()[0] - 23) // 35
                                    for i in range(coord[0] - 1, coord[0] + 2):
                                        for j in range(coord[1] - 1, coord[1] + 2):
                                            for kl in gr_kletka:
                                                if kl.rect.topleft == (j * 35 + 23, i * 35 + 120):
                                                    kl.kill()
                                            if 0 <= i < 16 and 0 <= j < 16:
                                                massive_kletki[i][j] = 1
                                    massive_test[coord[0]][coord[1]] = 1
                                    finded = True
                                    while finded:  # алгоритм поиска прилежащих пустых полей
                                        finded = False
                                        for i in range(stroki):
                                            for j in range(stolb):
                                                if massive_kletki[i][j] == 1 and massive[i][j] == 0 and massive_test[i][j] == 0:
                                                    finded = True
                                                    for m in range(i - 1, i + 2):
                                                        for n in range(j - 1, j + 2):
                                                            for kl in gr_kletka:
                                                                if kl.rect.topleft == (n * 35 + 23, m * 35 + 120):
                                                                    kl.kill()
                                                            if 0 <= m < 16 and 0 <= n < 16:
                                                                massive_kletki[m][n] = 1
                                                                massive_test[i][j] = 1
                                    sum_flag = 0
                                    for x in gr_kletka:  # подсчёт кол-вa установленых флагов
                                        if x.state == 1:
                                            sum_flag += 1
                                    count_bombs = bombs - sum_flag  # узнаём сколько осталось неоткрытых бомб
                                elif massive[(pygame.mouse.get_pos()[1] - 120) // 35][
                                    (pygame.mouse.get_pos()[0] - 23) // 35] == 9:  # если это бомба
                                    btn1.image = pygame.image.load("data/btn3.png").convert()
                                    btn1.state = 2  # меняем на смайл с крестами
                                    btn1.win = 0  # указываем, что проиграли
                                    timer = False  # останавливаем таймер
                                    for x in gr_sign:  # ищем бомбу, по которой щёлкнули и заменяем на красную
                                        if x.rect.collidepoint(pygame.mouse.get_pos()):
                                            bomb_rect = x.rect[0], x.rect[1]
                                            x.kill()
                                            gr_sign.add(Sign((bomb_rect), "data/bomb2.png"))
                                    vzruv = pygame.mixer.Sound("data/vzruv.ogg")
                                    vzruv.play()
                                    for i in range(stroki):  # открываем все бомбы
                                        for j in range(stolb):
                                            if massive[i][j] == 9:
                                                for x in gr_kletka:
                                                    if x.rect[:2] == [j * 35 + 23, i * 35 + 120]:
                                                        x.kill()
                                if btn1.win == 1:  # если идёт игра
                                    summa = 0
                                    for i in massive_kletki:
                                        summa += i.count(0)  # подсчитываем кол-во закрытых клеток
                                    if summa == bombs:  # если кол-во закрытых клеток равняется кол-ву бомб
                                        horaay = pygame.mixer.Sound("data/horaay.ogg")
                                        horaay.play()
                                        btn1.image = pygame.image.load("data/btn5.png").convert()
                                        btn1.win = 2  # говорим, что выиграли
                                        btn1.state = 3  # изображение в очках
                                        timer = False  # останавливаем таймер
                                        for x in gr_kletka:  # на всe бомбы ставим флаги
                                            x.image = pygame.image.load("data/flag.png").convert()
                                for kl in gr_kletka:
                                    if kl.rect.collidepoint(pygame.mouse.get_pos()):
                                        kl.kill()  # уничтожаем клетку, по которой щёлкнули

                else:  # если выиграли или проиграли
                    if btn1.rect.collidepoint(pygame.mouse.get_pos()):  # если попали по большой кнопке
                        btn1.image = pygame.image.load("data/btn4.png").convert()
                        btn1.state = 1  # меняем на нажатый смайл
    if timer:  # если таймер идёт
        second = str((pygame.time.get_ticks() - start) // 1000).zfill(
            3)  # получаем время в виде строки с начальными нулями
    window.blit(background, (0, 0))
    gr_sign.draw(window)
    gr_kletka.draw(window)
    window.blit(btn1.image, btn1.rect)
    str_bomb = str(count_bombs).zfill(3)
    clock1.update_digit(second[-3:-2])  # расчёт времени
    clock2.update_digit(second[-2:-1])
    clock3.update_digit(second[-1:])
    digit_1.update_digit(str_bomb[:1])  # расчёт бомб
    digit_2.update_digit(str_bomb[1:2])
    digit_3.update_digit(str_bomb[2:])
    window.blit(digit_1.image, digit_1.rect)  # вывод на экран бомб и часов
    window.blit(digit_2.image, digit_2.rect)
    window.blit(digit_3.image, digit_3.rect)
    window.blit(clock1.image, clock1.rect)
    window.blit(clock2.image, clock2.rect)
    window.blit(clock3.image, clock3.rect)
    pygame.display.update()
    clock.tick(50)