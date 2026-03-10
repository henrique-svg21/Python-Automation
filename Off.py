import pyautogui as py
import time
py.FAILSAFE = True

#ao rodar o comando durante a manha, automaticamente desligará o pc em 6 horas e 50 minutos.
#Rodar de manha logo quando ligar o pc

py.hotkey('win', 'r')
time.sleep(0.5)
py.write('cmd')
time.sleep(0.5)
py.press('enter')
time.sleep(0.5)
py.write('shutdown /s /t 24600')
time.sleep(0.5)
py.press('enter')
time.sleep(0.5)
py.hotkey('alt', 'f4')
