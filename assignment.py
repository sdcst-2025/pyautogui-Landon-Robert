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
        pyautogui.locateOnScreen("Assets/goldenCookie2.png", confidence=0.5)
        pyautogui.moveTo(pyautogui.locateOnScreen("Assets/goldenCookie2.png", confidence=0.5))
        pyautogui.click()
    except:
        try:
            if pyautogui.locateOnScreen("Assets/upgradeActive.png", confidence=0.87):
                pyautogui.moveTo(pyautogui.locateOnScreen("Assets/upgradeActive2.png", confidence=0.87))
                pyautogui.click()
        except:
            try:
                pyautogui.locateOnScreen("Assets/buttonActive2.png", confidence=0.87)
                pyautogui.moveTo(pyautogui.locateOnScreen("Assets/buttonActive2.png", confidence=0.9))
                pyautogui.click(clicks=10, interval=0.02)
            except:
                pyautogui.moveTo(cookiePos)
                pyautogui.click(clicks=100, interval=0.02)

    if keyboard.is_pressed("q"):
        run = False
    else:
        pass
