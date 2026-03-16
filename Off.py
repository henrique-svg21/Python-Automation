import pyautogui as py
import time
from datetime import datetime, timedelta

agora = datetime.now()
alvo = agora.replace(hour=14, minute=28, second=0, microsecond=0)

if agora > alvo:
    alvo += timedelta(days=1)

segundos_faltantes = int((alvo - agora).total_seconds())

print(f"Agora são: {agora.strftime('%H:%M:%S')}")
print(f"Desligamento agendado para: {alvo.strftime('%d/%m %H:%M:%S')}")
print(f"Segundos até lá: {segundos_faltantes}")

py.FAILSAFE = True

py.hotkey('win', 'r')
time.sleep(1)
py.write('cmd')
time.sleep(1)
py.press('enter')
time.sleep(1.0) 

py.write(f'shutdown /s /t {segundos_faltantes}')
time.sleep(1)
py.press('enter')

time.sleep(1)
py.hotkey('alt', 'f4')

# aviso de confirmacao
py.alert(text=f'PC agendado para desligar às 14:25 (em {segundos_faltantes} segundos).', title='Agendamento Concluído')

