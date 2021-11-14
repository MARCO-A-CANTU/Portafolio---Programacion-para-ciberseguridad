import pyautogui
import webbrowser
import time
from faker import Faker
fake = Faker()

#Pregunta 1
opcion = int(input("Marvel o DC:\n [1] Marvel\n [2] DC\n [3] Ambas\n [4] Ninguna\n Digite una opcion: "))

# Pregunta 2
opcion2 = input("Escribe un refrán, catchphrase, dicho popular o cita de libro o película: ")

#Pregunta 3
opcion3 = int(input("Cuál es la mejor hora del día para comer pastel:\n [1] 8am\n [2] 9am\n [3] 10am\n [4] 11am\n [5] 12pm\n [6] 1pm\n [7] 2pm\n [8] 3pm\n [9] 4pm\n [10] 5pm\n [11] 6pm\n [12] Despues de las 7\n Digite una opcion: "))

url = "https://forms.office.com/r/S8Jy6Jsvmh"
# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)
time.sleep(12)
for i in range(1,5):
    pyautogui.press('tab')

# Respuesta 1
if opcion == 1:
    pyautogui.press('down')
    pyautogui.press('up')
if opcion == 2:
    pyautogui.press('down')
if opcion == 3:
    pyautogui.press('down')
    pyautogui.press('down')
if opcion == 4:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')

pyautogui.press('tab')
pyautogui.press('tab')

# Respuesta 2
pyautogui.write(opcion2)

pyautogui.press('tab')
pyautogui.press('tab')

# Respuesta 3

if opcion3 == 1:
    pyautogui.press('down')
if opcion3 == 2:
    pyautogui.press('down')
    pyautogui.press('down')
if opcion3 == 3:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
if opcion3 == 4:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
if opcion3 == 5:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
if opcion3 == 6:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
if opcion3 == 7:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
if opcion3 == 8:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
if opcion3 == 9:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
if opcion3 == 10:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
if opcion3 == 11:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
if opcion3 == 12:
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')

pyautogui.press('tab')
pyautogui.press('tab')

# Respuesta 4
opcion4 = fake.email()
print(opcion4)
pyautogui.write(opcion4)

time.sleep(20)
pyautogui.press('tab')
pyautogui.press('enter')