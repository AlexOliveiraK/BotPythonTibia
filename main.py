import pyautogui as pg
import keyboard as kb
import time
from distancia import Distancia
from battleTeste import Battle
from comer import Comer
from gastarMana import GastaMana

REGION = 1750, 25, 120, 120
MARCAS = ["estrela", "boca", "crus"]
CENTRO = pg.locateOnScreen('./MAPS/centro.png', confidence=0.8, region=REGION)

countHunt = 0
while(countHunt < 10):
    print("Volta na Hunt count >>> ", countHunt)
    
    if (CENTRO != None):
        CENTROX, CENTROY = pg.center(CENTRO)
        Comer()
        quantidade = len(MARCAS)
        enum = 0

        while (enum < quantidade):
            GastaMana()
            marca = MARCAS[enum]
            print(marca)
            CAMINHO =  "./MAPS/{0}.png".format(marca)
            regiao = pg.locateOnScreen(CAMINHO, confidence=0.8, region=REGION)
            if(regiao is not None):
                regiaoX, regiaoY = pg.center(regiao)
                destino = Distancia((CENTROX, CENTROY), (regiaoX, regiaoY))
                while (destino > 5):
                    pg.moveTo(regiaoX, regiaoY)
                    pg.click()

                    time.sleep(3)
     
                    regiao = pg.locateOnScreen(CAMINHO, confidence=0.8, region=REGION)
                    regiaoX, regiaoY = pg.center(regiao)
                    destino = Distancia((CENTROX, CENTROY), (regiaoX, regiaoY))
                    
                    print("BATTLE CHAMADO")
                    Battle()

            enum += 1
        count = 0
    else:
        print("Posição do boneco nao encontrada")
        
    countHunt+=1