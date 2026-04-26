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
    "tCamisaChica":(0.6703125, 0.5347222222222222),
    "puertaBunny":(0.34609375 ,0.4097222222222222),
    "menuPrincipal":(0.1390625,0.11388888888888889),
    "estrellaUno":(0.15546875,0.4736111111111111),
    "estrellaDos":(0.21640625,0.4791666666666667),
    "estrellaTres":(0.27421875,0.4736111111111111255),
    "letraM":(0.55625, 0.44583333333333336),
    "newGame":(0.13828125, 0.5652777777777778),
    "continueGame":(0.17890625, 0.6791666666666667),
    "noche6":(0.21640625, 0.7861111111111111),
    "customNight":(0.20078125, 0.8694444444444445),
    "botonFreddy":(0.23828125, 0.6888888888888889),
    "botonBonnie":(0.46015625, 0.6888888888888889255),
    "botonChica":(0.67734375, 0.6875),
    "botonFoxy":(0.89375, 0.6875),
    "botonReady":(0.90078125, 0.9125)
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
            cinematicaNoche = False
            beatGame = False
            while(beatGame == False):
                contadorestrella1=0
                contadorestrella2=0
                contadorestrella3=0
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
                        int(cordenadas["estrellaDos"][0] * pyautogui.size()[0]),
                        int(cordenadas["estrellaDos"][1] * pyautogui.size()[1]),
                        (255, 255, 255)):
                        contadorestrella2+=1
                    else:
                        break 
                for i in range(10):
                    if pyautogui.pixelMatchesColor(
                        int(cordenadas["estrellaTres"][0] * pyautogui.size()[0]),
                        int(cordenadas["estrellaTres"][1] * pyautogui.size()[1]),
                        (255, 255, 255)):
                        contadorestrella3+=1
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

                if(contadorestrella1 == 10):
                    estrellas+=1
                if(contadorestrella2 == 10):
                    estrellas+=1
                if(contadorestrella3 == 10):
                    estrellas+=1

                if(estrellas==0):
                    if(contadorContinue==10):
                        mousemove(cordenadas["continueGame"][0],cordenadas["continueGame"][1],0)
                        time.sleep(0.3)
                        pyautogui.click()
                        menuprincipal=False
                    else:
                        mousemove(cordenadas["newGame"][0],cordenadas["newGame"][1],0)
                        time.sleep(0.3)
                        pyautogui.click()
                        menuprincipal=False
                
                elif(estrellas==1):
                    mousemove(cordenadas["noche6"][0],cordenadas["noche6"][1],0)
                    time.sleep(0.3)
                    pyautogui.click()
                    menuprincipal=False
                elif(estrellas==2):
                    mousemove(cordenadas["customNight"][0],cordenadas["customNight"][1],0)
                    time.sleep(0.3)
                    pyautogui.click()
                    time.sleep(0.3)
                    mousemove(cordenadas["botonFreddy"][0],cordenadas["botonFreddy"][1],0)
                    for i in range(25):
                        pyautogui.click()
                        time.sleep(0.3)
                    time.sleep(0.3)
                    mousemove(cordenadas["botonBonnie"][0],cordenadas["botonBonnie"][1],0)
                    for i in range(20):
                        pyautogui.click()
                        time.sleep(0.3)
                    time.sleep(0.3)
                    mousemove(cordenadas["botonChica"][0],cordenadas["botonChica"][1],0)
                    for i in range(20):
                        pyautogui.click()
                        time.sleep(0.3)
                    time.sleep(0.3)
                    mousemove(cordenadas["botonFoxy"][0],cordenadas["botonFoxy"][1],0)
                    for i in range(25):
                        pyautogui.click()
                        time.sleep(0.3)
                    time.sleep(0.3)
                    mousemove(cordenadas["botonReady"][0],cordenadas["botonReady"][1],0)
                    time.sleep(0.3)                    
                    pyautogui.click()
                    menuprincipal=False
                elif(estrellas==3):
                    beatGame=True
                
                while menuprincipal==False:
                    global puertaDerechaRojo
                    cam4B=False
                    global puertaIzquierdaRojo
                    puertaIzquierdaRojo=True
                    puertaDerechaRojo=True
                    cinematicaNoche = comprobarCinematicaNoche()
                    mousemove(cordenadas["botonLuzIzquierda"][0],cordenadas["botonLuzIzquierda"][1],0)
                    time.sleep(9)
                    while(cinematicaNoche == False):
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
                        pyautogui.click()
                        for i in range(15):
                            if pyautogui.pixelMatchesColor(
                            int(cordenadas["puertaBunny"][0] * pyautogui.size()[0]),
                            int(cordenadas["puertaBunny"][1] * pyautogui.size()[1]),
                            (0, 0, 0)):
                                contadorbonnie+=1
                            else:
                                break
                        if contadorbonnie==15:
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
                        mousemove(cordenadas["botonLuzDerecha"][0],cordenadas["botonLuzDerecha"][1],0)
                        time.sleep(0.4)
                        pyautogui.click()
                        for i in range(25):
                            if pyautogui.pixelMatchesColor(
                            int(cordenadas["tCamisaChica"][0] * pyautogui.size()[0]),
                            int(cordenadas["tCamisaChica"][1] * pyautogui.size()[1]),
                            (86, 95, 9)):
                                contadorchica+=1
                            else:
                                break
                        #print("Contador chica: " + str(contadorchica))
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
                        time.sleep(0.3)
                        cinematicaNoche = comprobarCinematicaNoche()

    except AttributeError:
        print()

def comprobarCinematicaNoche():
    contadorFinNoche=0
    cinematicaNoche = False
    for i in range(10):
        if pyautogui.pixelMatchesColor(
        int(cordenadas["letraM"][0] * pyautogui.size()[0]),
        int(cordenadas["letraM"][1] * pyautogui.size()[1]),
        (0, 0, 0)):
            contadorFinNoche+=1
        else:
            break
    if(contadorFinNoche == 10):
        cinematicaNoche = True
    return cinematicaNoche

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