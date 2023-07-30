import pyautogui as pg


REGION = 1743, 551, 100, 100
SEMBICHO = "./BATTLE/semBicho.png"
ATACANDO = "./BATTLE/atacando.png"
CENTRO = pg.locateOnScreen('./MAPS/centro.png', confidence=0.8, region=REGION)

count = 0

while(count < 5):
    x1, y1 = pg.center(REGION)
    pg.moveTo(x1, y1, 1)
    noBattle = pg.locateOnScreen(SEMBICHO, confidence=0.9)
    print(noBattle)

    count += 1
