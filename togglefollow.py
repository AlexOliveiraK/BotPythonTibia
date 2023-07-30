import pyautogui as pg

FOLLOW = "./BATTLE/follow.png"
NO_FOLLOW = "./BATTLE/noFollow.png"

REGIAO = (1820, 150, 500, 100)

def Seguir(seguir):

    ESTA_SEGUINDO = pg.locateOnScreen(FOLLOW, confidence=0.7)

    if(seguir and ESTA_SEGUINDO is None):
        pg.press('p')

Seguir(True)
