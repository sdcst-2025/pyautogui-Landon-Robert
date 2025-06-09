import webbrowser
import pyautogui
import keyboard
import time
"""
#webbrowser.open("https://orteil.dashnet.org/cookieclicker/")
"""

print(pyautogui.locateOnScreen("Assets/goldenCookie.png", confidence=0.5))
run = True
while run == True:
    cookiePos = pyautogui.locateOnScreen('Assets/cookie2.png', confidence=0.7)
    try: 
        pyautogui.locateOnScreen("Assets/goldenCookie.png", confidence=0.5)
        pyautogui.moveTo(pyautogui.locateOnScreen("Assets/goldenCookie.png", confidence=0.5))
        pyautogui.click()
    except:
        try:
            pyautogui.locateOnScreen("Assets/upgradeActive.png", confidence=0.5)
            pyautogui.moveTo(pyautogui.locateOnScreen("Assets/upgradeActive.png", confidence=0.5))
            pyautogui.click()
        except:
            try:
                pyautogui.locateOnScreen("Assets/buttonActive2.png", confidence=0.5)
                pyautogui.moveTo(pyautogui.locateOnScreen("Assets/buttonActive2.png", confidence=0.5))
                pyautogui.click()
            except:
                pyautogui.moveTo(cookiePos)
                pyautogui.click(clicks=100, interval=0.1)

    if keyboard.is_pressed("q"):
        break
