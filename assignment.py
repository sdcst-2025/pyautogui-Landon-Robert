import webbrowser
import pyautogui
import keyboard
import time

#webbrowser.open("https://orteil.dashnet.org/cookieclicker/")
run = 0
while run < 30:
    cookiePos = pyautogui.locateOnScreen('Assets/cookie2.png', confidence=0.7)
    print(cookiePos)
    pyautogui.moveTo(cookiePos)
    pyautogui.click(clicks=100, interval=0.01)
    ## time.sleep(0.01)
    ## pyautogui.moveTo(10,10)
    ## time.sleep(0.01)
    run = run + 1



run = True
while run == True:
    


    if keyboard.is_pressed("q"):
        break
