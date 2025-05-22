import webbrowser
import pyautogui
import keyboard

webbrowser.open("https://orteil.dashnet.org/cookieclicker/")
pyautogui.moveTo(1,1)

run = True
while run == True:
    


    if keyboard.is_pressed("q"):
        break