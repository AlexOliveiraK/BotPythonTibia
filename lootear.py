import pyautogui as pyg
import mouse as pg
import time

from togglefollow import Seguir

X = 1320
Y = 400

def Lootea():
    
    Seguir(False)
    
    pg.move(X, Y)
    pyg.rightClick()
    
    #top
    pg.move(X, Y-50)
    pyg.rightClick()
    
    #top-esquerda
    pg.move(X-50, Y-50)
    pyg.rightClick()

    #esquerda
    pg.move(X-50, Y)
    pyg.rightClick()

    #botton-esquerda
    pg.move(X-50, Y+50)
    pyg.rightClick()

    #botton
    pg.move(X, Y+50)
    pyg.rightClick()

    #botton-direita
    pg.move(X+50, Y+50)
    pyg.rightClick()

    #direita
    pg.move(X+50, Y)
    pyg.rightClick()

    #top-direita
    pg.move(X+50, Y-50)
    pyg.rightClick()
    
    time.sleep(1)
    
    Seguir(True)
    
Lootea()