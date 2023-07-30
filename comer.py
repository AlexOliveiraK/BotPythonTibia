import pyautogui as pg
import time

def Comer():
    REGIAO = (1750, 150, 200, 400)
    FOME = "./FOME/fome.png"

    ESTA_COM_FOME = pg.locateOnScreen(FOME, confidence=0.7, region=REGIAO)
    
    print(ESTA_COM_FOME)
    
    if(ESTA_COM_FOME is not None):
        pg.press('o')
        time.sleep(0.5)
        pg.press('o')
        time.sleep(0.5)
        pg.press('o')
        time.sleep(0.5)
        
time.sleep(2)
Comer()