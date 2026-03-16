import os
import time
from datetime import datetime, timedelta
import pyautogui as py

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import credentials from your separate file
import Credentials

def schedule_shutdown():
    """Calculates the time until 14:28 and schedules a system shutdown."""
    agora = datetime.now()
    alvo = agora.replace(hour=14, minute=28, second=0, microsecond=0)

    # If it's already past 14:28 today, schedule for tomorrow
    if agora > alvo:
        alvo += timedelta(days=1)

    segundos_faltantes = int((alvo - agora).total_seconds())

    print(f"Agora são: {agora.strftime('%H:%M:%S')}")
    print(f"Desligamento agendado para: {alvo.strftime('%d/%m %H:%M:%S')}")
    print(f"Segundos até lá: {segundos_faltantes}")

    # Directly execute the shutdown command in the background
    os.system(f'shutdown /s /t {segundos_faltantes}')

    # Confirmation alert
    py.alert(text=f'PC agendado para desligar às 14:28 (em {segundos_faltantes} segundos).', title='Agendamento Concluído')


def open_and_log_in():
    """Opens Chrome incognito and logs into Google, Gemini, GitHub, and SENAI."""
    chrome_options = Options()

    # Open in Incognito & Dark Mode
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--force-dark-mode")
    chrome_options.add_argument("--enable-features=WebUIDarkMode")
    chrome_options.add_experimental_option("detach", True)

    # Hide basic automation banners
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    servicce = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=servicce, options=chrome_options)

    # ==========================================
    # 1. GOOGLE LOGIN (Tab 1 - Index 0)
    # ==========================================
    browser.get("https://accounts.google.com/")

    email_input = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.ID, "identifierId"))
    )
    email_input.send_keys(Credentials.email + Keys.ENTER)

    password_input = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    time.sleep(1)
    password_input.send_keys(Credentials.password + Keys.ENTER)
    time.sleep(5)
    
    browser.get("https://www.gmail.com")

    # ==========================================
    # 2. GEMINI LOGIN (Tab 2 - Index 1)
    # ==========================================
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("https://gemini.google.com/app")

    WebDriverWait(browser, 10).until(
        EC.url_contains("gemini.google.com")
    )
    time.sleep(3) 
    print("Successfully opened Gemini!")

    # ==========================================
    # 3. GITHUB LOGIN (Tab 3 - Index 2)
    # ==========================================
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[2])
    browser.get("https://github.com/login")
    print("Navigated to GitHub login page...")

    try:
        github_user_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "login_field"))
        )
        github_user_input.send_keys(Credentials.github_email)

        github_pass_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        github_pass_input.send_keys(Credentials.github_password + Keys.ENTER)
        print("Sent GitHub credentials!")

        WebDriverWait(browser, 15).until(
            EC.url_to_be("https://github.com/")
        )
        print("Successfully logged into GitHub!")
    except Exception as e:
        print("GitHub Login might have failed. Check the browser.", e)

    # ==========================================
    # 4. SENAI ESPAÇO DO ESTUDANTE (Tab 4 - Index 3)
    # ==========================================
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[3])
    browser.get("https://estudante.sesisenai.org.br/login")
    print("Navigated to Espaço do Estudante SENAI...")

    try:
        # 1. Wait for the PRESENCE of the hidden Flutter input box using the ID you found
        senai_user_input = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        
        # 2. Use JavaScript to forcefully focus on this hidden element
        browser.execute_script("arguments[0].focus();", senai_user_input)
        time.sleep(0.5) 
        
        # 3. Type the user, TAB to the password, and hit ENTER
        senai_user_input.send_keys(Credentials.senai_user + Keys.TAB + Credentials.senai_password + Keys.ENTER)
        
        print("Sent SENAI credentials!")
        time.sleep(5) # Buffer to let the dashboard load
        
    except Exception as e:
        print("Failed to interact with the hidden SENAI login fields.", e)
    # ==========================================
    # 5. FINAL GOOGLE TAB (Tab 5 - Index 4)
    # ==========================================
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[4])
    browser.get("https://www.google.com")
    print("Final Google tab opened.")


# ==========================================
# MAIN EXECUTION BLOCK
# ==========================================
if __name__ == "__main__":
    print("Starting automation routine...")
    
    # Run the shutdown scheduler first
    schedule_shutdown()
    
    # Then launch the browser routines
    open_and_log_in()
    
    print("Automation routine finished successfully!")