import pygame
import math

pygame.init()

szerokosc = 600
wysokosc = 600
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("GK_Lab2_ZAD1")

bialy = (255, 255, 255)
zolty = (255, 255, 0)
czarny = (0, 0, 0)

promien = 150
srodek_x = szerokosc // 2
srodek_y = wysokosc // 2
kat_obrotu = -math.pi / 2

def rysuj_pieciokat(powierzchnia, kolor, srodek, promien, kat_poczatkowy=0):
    punkty = []
    for i in range(5):
        kat = kat_poczatkowy + 2 * math.pi * i / 5
        x = srodek[0] + promien * math.cos(kat)
        y = srodek[1] + promien * math.sin(kat)
        punkty.append((x, y))
    pygame.draw.polygon(powierzchnia, kolor, punkty)

dziala = True
while dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        if zdarzenie.type == pygame.KEYDOWN:

            if zdarzenie.key == pygame.K_1:
                promien = 150
                srodek_x = szerokosc // 2
                srodek_y = wysokosc // 2
                kat_obrotu = -math.pi / 2

            elif zdarzenie.key == pygame.K_2:
                promien = 150
                srodek_x = szerokosc // 2
                srodek_y = wysokosc // 2
                kat_obrotu = -math.pi / 2 + math.radians(30)

            elif zdarzenie.key == pygame.K_3:
                promien = 150
                srodek_x = szerokosc // 2
                srodek_y = wysokosc // 2
                kat_obrotu = -math.pi / 2 + math.pi

            elif zdarzenie.key == pygame.K_4:
                promien = 150
                srodek_x = szerokosc // 2
                srodek_y = wysokosc // 2
                kat_obrotu = -math.pi / 2 - math.radians(15)

            elif zdarzenie.key == pygame.K_5:
                promien = 150
                srodek_x = szerokosc // 2
                srodek_y = promien
                kat_obrotu = -math.pi / 2

            elif zdarzenie.key == pygame.K_6:
                promien = 150
                srodek_x = szerokosc // 2
                srodek_y = wysokosc // 2
                kat_obrotu = -math.pi / 2 + math.radians(80)

            elif zdarzenie.key == pygame.K_7:
                promien = 150
                srodek_x = szerokosc // 2
                srodek_y = wysokosc // 2
                kat_obrotu = -math.pi / 2 + math.pi

            elif zdarzenie.key == pygame.K_8:
                promien = 150
                srodek_x = 200
                srodek_y = 400
                kat_obrotu = -math.pi / 2 + math.radians(20)

            elif zdarzenie.key == pygame.K_9:
                promien = 150
                srodek_x = 476
                srodek_y = wysokosc // 2
                kat_obrotu = -math.pi / 2 + math.radians(200)

    ekran.fill(zolty)
    rysuj_pieciokat(ekran, czarny, (srodek_x, srodek_y), promien, kat_poczatkowy=kat_obrotu)

    pygame.display.flip()

pygame.quit()
