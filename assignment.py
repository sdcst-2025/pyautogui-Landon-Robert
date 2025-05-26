import webbrowser
import pyautogui
import keyboard

webbrowser.open("https://orteil.dashnet.org/cookieclicker/")
cookiePos = pyautogui.locateOnScreen('cookie.png', confidence=0.7)
print(cookiePos)
pyautogui.moveTo(cookiePos)

"""
run = True
while run == True:
    


    if keyboard.is_pressed("q"):
        break
"""