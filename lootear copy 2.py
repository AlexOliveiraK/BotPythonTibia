import mouse as pg
import time

from togglefollow import Seguir

X = 1320
Y = 400

def Lootea():
    
    Seguir(False)
    
    pg.move(X, Y, absolute=True, duration=0.01)
    pg.right_click()

    time.sleep(1)
    #top
    pg.move(X, Y-50, absolute=True, duration=0.01)
    pg.right_click()

    #top-esquerda
    pg.move(X-50, Y-50, absolute=True, duration=0.01)
    pg.right_click()

    #esquerda
    pg.move(X-50, Y, absolute=True, duration=0.01)
    pg.right_click()

    #botton-esquerda
    pg.move(X-50, Y+50, absolute=True, duration=0.01)
    pg.right_click()

    #botton
    pg.move(X, Y+50, absolute=True, duration=0.01)
    pg.right_click()

    #botton-direita
    pg.move(X+50, Y+50, absolute=True, duration=0.01)
    pg.right_click()

    #direita
    pg.move(X+50, Y, absolute=True, duration=0.01)
    pg.right_click()

    #top-direita
    pg.move(X+50, Y-50, absolute=True, duration=0.01)
    pg.right_click()

    Seguir(True)
    
Lootea()