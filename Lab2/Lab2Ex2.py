import pygame

pygame.init()

szerokosc = 600
wysokosc = 600
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("GK_LAB2_ZAD2")

BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

def rysunek1(powierzchnia):
    pygame.draw.circle(powierzchnia, CZARNY, (150, 150), 100)
    pygame.draw.rect(powierzchnia, ZOLTY, (100, 100, 100, 100))

def rysunek2(powierzchnia):
    pygame.draw.rect(powierzchnia, ZIELONY, (350, 50, 150, 200))
    pygame.draw.polygon(powierzchnia, BIALY, [(350, 250), (425, 125), (500, 250)])

def rysunek3(powierzchnia):
    pygame.draw.polygon(powierzchnia, FIOLETOWY, [(130, 375), (155, 400), (180, 375)])
    pygame.draw.polygon(powierzchnia, FIOLETOWY, [(130, 490), (155, 465), (180, 490)])
    pygame.draw.rect(powierzchnia, FIOLETOWY, (80, 400, 150, 65))

def rysuj_obrocony_prostokat(powierzchnia, kolor, x, y, szerokosc, wysokosc, kat):

    prostokat = pygame.Surface((szerokosc, wysokosc), pygame.SRCALPHA)
    prostokat.fill(kolor)

    obrocony_prostokat = pygame.transform.rotate(prostokat, kat)

    obwiednia = obrocony_prostokat.get_rect()
    obwiednia.center = (x, y)

    powierzchnia.blit(obrocony_prostokat, obwiednia.topleft)

def rysunek4(powierzchnia):
    pygame.draw.rect(powierzchnia, CZERWONY, (350, 375, 150, 10))
    rysuj_obrocony_prostokat(ekran, CZERWONY, 425, 441, 190, 10, 40)
    pygame.draw.rect(powierzchnia, CZERWONY, (350, 500, 150, 10))

dziala = True
while dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False

    ekran.fill(BIALY)

    rysunek1(ekran)
    rysunek2(ekran)
    rysunek3(ekran)
    rysunek4(ekran)

    pygame.display.flip()

pygame.quit()
