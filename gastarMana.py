import pyautogui as pg
import time 
def GastaMana():
    MANA_CHEIA = "./MANA/manaCheia2.png"

    REGIAO = (1300, 10, 100, 100)

    MANA_ESTA_CHEIA = pg.locateOnScreen(MANA_CHEIA, confidence=0.9, region=REGIAO)

    if(MANA_ESTA_CHEIA is not None):
        pg.press("f4")

time.sleep(2)
GastaMana()
