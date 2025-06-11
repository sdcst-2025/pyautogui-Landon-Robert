import webbrowser
import pyautogui
import keyboard
import time

"""
webbrowser.open("https://orteil.dashnet.org/cookieclicker/")
"""

run = True
cookiePos = pyautogui.locateOnScreen('Assets/cookie2.png', confidence=0.8)
while run == True:
    try:
        pyautogui.locateOnScreen("Assets/goldenCookie.png", confidence=0.7)
        pyautogui.moveTo(pyautogui.locateOnScreen("Assets/goldenCookie.png", confidence=0.7))
        pyautogui.click()
    except:
        try:
            pyautogui.locateOnScreen("Assets/upgradeActive.png", confidence=0.9)
            pyautogui.moveTo(pyautogui.locateOnScreen("Assets/upgradeActive.png", confidence=0.9))
            pyautogui.click()
            time.sleep(0.1)
        except:
            try:
                pyautogui.locateOnScreen("Assets/buttonActive4.png", confidence=0.9)
                pyautogui.moveTo(pyautogui.locateOnScreen("Assets/buttonActive4.png", confidence=0.9))
                pyautogui.click(clicks=10, interval=0.1)
            except:
                pyautogui.moveTo(cookiePos)
                pyautogui.click(clicks=100, interval=0.1)

    if keyboard.is_pressed("q"):
        run = False
    else:
        pass
