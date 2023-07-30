import pyautogui as pg

def Distancia (ponto1, ponto2):

    x1, y1 = ponto1
    x2, y2 = ponto2

    if(x1 < 1):
        x1 = x1 * -1

    if(x1 < 1):
        y1 = y1 * -1

    if(x2 < 1):
        x2 = x2 * -1

    if(y1 < 1):
        y1 = y1 * -1

    Xa = x1 - x2
    Ya = y1 - y2

    if(Xa < 1):
        Xa = Xa * -1

    if(Ya < 1):
        Ya = Ya * -1

    distancia = (Xa*2) + (Ya*2)

    print("Distancia: ", distancia)
    
    distancia = distancia ** (1/2)

    if(distancia < 0):
        distancia += distancia * -1
   
    return distancia
