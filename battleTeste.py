import pyautogui as pg
import time
from lootear import Lootea
from togglefollow import Seguir

def Battle():

    REGION = 1500, 200, 1000, 1000
    BATTLESEMBICHO = "./BATTLE/semBicho.png"
    BATTLE = "./BATTLE/battle.png"
    #BATTLING = "./BATTLE/atacando.png"
    #BATTLING2 = "./BATTLE/atacando2.png"
    BATTLING3 = "./BATTLE/atacando4.png"

    def LocalizaBattle():
        BATTLE_LOCATION = pg.locateOnScreen(BATTLE, confidence=0.8, region=REGION)
        if(BATTLE_LOCATION is not None):
            #print("battle location", BATTLE_LOCATION)    
            return True
        else:
            print("Battle não encontrado")
            return False

    def VerificaSeTemBichoNoBattle():
        BATTLE_SEM_BICHO = pg.locateOnScreen(BATTLESEMBICHO, confidence=0.9)
        #pg.moveTo(BATTLE_SEM_BICHO)
        if(BATTLE_SEM_BICHO is None):
            print("Tem bicho")
        else:
            print("Não tem bicho no battle")
        
        return BATTLE_SEM_BICHO

    if(LocalizaBattle()):
    
        battle_vazio = VerificaSeTemBichoNoBattle()
        
        batalhou = False
        countBatalha = 0
        
        while(battle_vazio is None):
            print("Tem bicho")
            batalhou = True            
            emBatalha = pg.locateOnScreen(BATTLING3, confidence=0.9, region=(battle_vazio))
            if emBatalha is not None:
                print("emBatalha")
                time.sleep(1)
            else:
                print("não esta atacando")
                Seguir(True)
                pg.press('space')
                Seguir(True)
                Lootea()
                
            countBatalha+=1
            if countBatalha > 10: break
            
            battle_vazio = VerificaSeTemBichoNoBattle()
        
        if batalhou: Lootea()
            

Battle()