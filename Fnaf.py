import pyautogui
import time
from pynput import keyboard

puertaIzquierdaRojo=True
puertaDerechaRojo=True

cordenadas={
    "botonPuertaIzquierda":(0.0453125,0.4652777777777778),
    "botonLuzIzquierda":(0.04375,0.6277777777777778),
    "botonPuertaDerecha":(0.95234375,0.4930555555555556),
    "botonLuzDerecha":(0.9484375,0.6472222222222223),
    "camara4B": (0.846875, 0.8944444444444445),
    "entrarCamara":(0.4125,0.9277777777777778),
    "salirCamara":(0.45390625,0.8222222222222222),
    "sCamisaChica":(0.6875, 0.5027777777777778),
    "puertaBunny":(0.34609375 ,0.4097222222222222),
    "menuPrincipal":(0.1390625,0.11388888888888889),
    "estrellaUno":(0.15546875,0.4736111111111111),
    "estrellaDos":(0.21640625,0.4791666666666667),
    "estrellaTres":(0.27421875,0.4736111111111111255),
    "letraM":(0.55625, 0.44583333333333336),
    "newGame":(0.13828125, 0.5652777777777778),
    "continueGame":(0.17890625, 0.6791666666666667),
}

def onPress(key):
    try:
        if(key.char=='p'):
            w,h=pyautogui.size()
            pyautogui.position().x
            print(pyautogui.position().x/w,pyautogui.position().y/h)
            x, y = pyautogui.position()
            color = pyautogui.pixel(x, y)
            print(f"X:{x} Y:{y} Color:{color}", end="\r")
        if(key.char=='m'):
            cam4B=False
            menuprincipal=False
            contadorFoxy=0
            contadorestrella1=0
            contadorContinue=0
            estrellas=0
            for i in range(10):
                if pyautogui.pixelMatchesColor(
                    int(cordenadas["estrellaUno"][0] * pyautogui.size()[0]),
                    int(cordenadas["estrellaUno"][1] * pyautogui.size()[1]),
                    (255, 255, 255)):
                    contadorestrella1+=1
                else:
                    break  
            for i in range(10):
                if pyautogui.pixelMatchesColor(
                    int(cordenadas["continueGame"][0] * pyautogui.size()[0]),
                    int(cordenadas["continueGame"][1] * pyautogui.size()[1]),
                    (255, 255, 255)):
                    contadorContinue+=1
                else:
                    break
            if(contadorestrella1!=10):
                if(contadorContinue==10):
                    mousemove(cordenadas["continueGame"][0],cordenadas["continueGame"][1],0)
                    time.sleep(0.3)
                    pyautogui.click()
                else:
                    mousemove(cordenadas["newGame"][0],cordenadas["newGame"][1],0)
                    time.sleep(0.3)
                    pyautogui.click()
            else:
                estrellas+=1
                

            while menuprincipal==False:
                contadorbonnie=0
                contadorchica=0
                if pyautogui.pixelMatchesColor(
                    int(cordenadas["menuPrincipal"][0] * pyautogui.size()[0]),
                    int(cordenadas["menuPrincipal"][1] * pyautogui.size()[1]),
                    (255, 255, 255)):
                    menuprincipal=True
                    break
                mousemove(cordenadas["botonLuzIzquierda"][0],cordenadas["botonLuzIzquierda"][1],0)
                time.sleep(0.3)
                global puertaIzquierdaRojo
                pyautogui.click()
                for i in range(20):
                    if pyautogui.pixelMatchesColor(
                    int(cordenadas["puertaBunny"][0] * pyautogui.size()[0]),
                    int(cordenadas["puertaBunny"][1] * pyautogui.size()[1]),
                    (0, 0, 0)):
                        contadorbonnie+=1
                    else:
                        break
                if contadorbonnie==20:
                    if(puertaIzquierdaRojo==True):
                        mousemove(cordenadas["botonPuertaIzquierda"][0],cordenadas["botonPuertaIzquierda"][1],0)
                        time.sleep(0.2)
                        pyautogui.click()
                        puertaIzquierdaRojo=False
                else:
                    if(puertaIzquierdaRojo==False):
                        mousemove(cordenadas["botonPuertaIzquierda"][0],cordenadas["botonPuertaIzquierda"][1],0)
                        time.sleep(0.2)
                        pyautogui.click()
                        puertaIzquierdaRojo=True
                cam4B=entrarCamara(cam4B)
                contadorFoxy+=1
                mousemove(cordenadas["botonLuzDerecha"][0],cordenadas["botonLuzDerecha"][1],0)
                time.sleep(0.4)
                pyautogui.click()
                global puertaDerechaRojo
                for i in range(20):
                    if pyautogui.pixelMatchesColor(
                    int(cordenadas["sCamisaChica"][0] * pyautogui.size()[0]),
                    int(cordenadas["sCamisaChica"][1] * pyautogui.size()[1]),
                    (105, 106, 13)):
                        contadorchica+=1
                    else:
                        break
                if contadorchica>1:
                    if(puertaDerechaRojo==True):
                        mousemove(cordenadas["botonPuertaDerecha"][0],cordenadas["botonPuertaDerecha"][1],0)
                        time.sleep(0.2)
                        pyautogui.click()
                        puertaDerechaRojo=False
                else:
                    if(puertaDerechaRojo==False):
                        mousemove(cordenadas["botonPuertaDerecha"][0],cordenadas["botonPuertaDerecha"][1],0)
                        time.sleep(0.2)
                        pyautogui.click()
                        puertaDerechaRojo=True    
                cam4B=entrarCamara(cam4B)
                contadorFoxy+=1
                if contadorFoxy>=40:
                    if(puertaIzquierdaRojo==True):
                        mousemove(cordenadas["botonPuertaIzquierda"][0],cordenadas["botonPuertaIzquierda"][1],0)
                        time.sleep(0.2)
                        pyautogui.click()
                        puertaIzquierdaRojo=False
                        contadorFoxy=0
                time.sleep(0.3)

    except AttributeError:
        print()

def mousemove(x,y,time):
    pyautogui.moveTo(x*pyautogui.size()[0],y*pyautogui.size()[1],time)
        

def entrarCamara(cam4B):
    mousemove(cordenadas["entrarCamara"][0],cordenadas["entrarCamara"][1],0)
    if cam4B==False:
        mousemove(cordenadas["camara4B"][0],cordenadas["camara4B"][1],0)
        time.sleep(0.3)
        pyautogui.click()
        cam4B=True
        mousemove(cordenadas["salirCamara"][0],cordenadas["salirCamara"][1],0)
    else:
        mousemove(cordenadas["salirCamara"][0],cordenadas["salirCamara"][1],0)
        time.sleep(0.3)
    mousemove(cordenadas["entrarCamara"][0],cordenadas["entrarCamara"][1],0)
    mousemove(cordenadas["salirCamara"][0],cordenadas["salirCamara"][1],0)
    return cam4B   

with keyboard.Listener(on_press=onPress) as listener:
    listener.join()