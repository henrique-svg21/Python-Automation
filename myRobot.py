import pyautogui as py
import time

py.press('win')
time.sleep(1)
py.write('bloco de notas')
time.sleep(1)
py.press('enter')
time.sleep(1)
py.write('@echo off \n for /L %%i in (1,1,100) do start chrome.exe "https://www.google.com"', interval = 0.1)
time.sleep(1)
py.hotkey('ctrl', 's')
time.sleep(1)
py.write('Discurso.bat')
time.sleep(1)
py.press('enter')
py.press('win')
time.sleep(1)
py.write('explorador de arquivos')
time.sleep(1)
py.press('enter')
time.sleep(1)
py.hotkey('ctrl', 'f')
time.sleep(1)
py.write('Discurso')





