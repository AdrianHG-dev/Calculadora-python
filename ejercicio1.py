import pyautogui
import pyperclip
import webbrowser
from time import sleep

#cantidad = int(input("Ingrese la cantidad de veces que quiera que aparezca: "))

mensaje = "Lo que sea"
pyautogui.PAUSE = 0.3

webbrowser.open("https://www.instagram.com/direct/inbox/")
sleep(5)

pyautogui.click(x=322, y=407)

for i in range(100): #cantidad de veces que quiera que aparezca o habilitar la variable "cantidad"
    pyperclip.copy(mensaje)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")



