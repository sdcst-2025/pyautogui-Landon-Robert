import webbrowser
import pyautogui
import keyboard
import time
"""
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
"""

run = True
while run == True:
    cookiePos = pyautogui.locateOnScreen('Assets/cookie2.png', confidence=0.7)
    if pyautogui.locateOnScreen("Assets/goldenCookie.png", confidence=0.5) != None:
        pyautogui.moveTo(pyautogui.locateOnScreen("Assets/goldenCookie.png", confidence=0.5))
        pyautogui.click()
    elif pyautogui.locateOnScreen("Assets/upgradeActive.png", confidence=0.5) != None:
        pyautogui.moveTo(pyautogui.locateOnScreen("Assets/upgradeActive.png", confidence=0.5))
        pyautogui.click()
    elif pyautogui.locateOnScreen("Assets/buttonActive.png", confidence=0.5) != None:
        pyautogui.moveTo(pyautogui.locateOnScreen("Assets/buttonActive.png", confidence=0.5))
        pyautogui.click()
    else:
        pyautogui.moveTo(cookiePos)
        pyautogui.click(clicks=100, interval=0.1)
    if keyboard.is_pressed("q"):
        break
