import pyautogui as py
import time
py.FAILSAFE = True

py.size()
(1366, 768)

py.press('win')
time.sleep(1)
py.write('bloco de notas', interval = 0.1)
time.sleep(1)
py.press('enter')
time.sleep(1)
py.write('@echo off \n for /L %%i in (1,1,10) do start chrome.exe "https://www.google.com"', interval = 0.1)
time.sleep(1)
py.hotkey('ctrl', 's')
time.sleep(1)
py.write('Discurso.bat', interval = 0.1)
time.sleep(1)
py.press('enter')
py.press('win')
time.sleep(1)
py.write('explorador de arquivos', interval = 0.1)
time.sleep(1)
py.press('enter')
time.sleep(1)
py.hotkey('ctrl', 'f')
time.sleep(1)
py.write('Discurso', interval = 0.1)
time.sleep(3)
py.click(x=621, y=252)
py.click(x=621, y=252)









