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
    now = datetime.now()
    target = now.replace(hour=14, minute=28, second=0, microsecond=0)

    # If it's already past 14:28 today, schedule for tomorrow
    if now > target:
        target += timedelta(days=1)

    remain_seconds = int((target - now).total_seconds())

    print(f"Now it is: {now.strftime('%H:%M:%S')}")
    print(f"Shutdown scheduled to: {target.strftime('%d/%m %H:%M:%S')}")
    print(f"Seconds remaining: {remain_seconds}")

    # Directly execute the shutdown command in the background
    os.system(f'shutdown /s /t {remain_seconds}')

    # Confirmation alert
    py.alert(text=f'Shutdown scheduled to 14:28 (in {remain_seconds} seconds).', title='SCHEDULE DONE')


def open_and_log_in():
    """Opens Chrome incognito and logs into Google, Gemini, GitHub, and SENAI."""
    chrome_options = Options()

    # Open in Incognito & Dark Mode
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--force-dark-mode")
    chrome_options.add_argument("--enable-features=WebUIDarkMode")
    chrome_options.add_argument("--start-maximized")
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
    # 4. AVA SESI SENAI (Tab 4 - Index 3)
    # ==========================================
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[3])
    browser.get("https://ava.sesisenai.org.br/login/index.php")
    print("Navigated to AVA SESI SENAI login page...")

    try:
        # Username field (standard Moodle ID)
        ava_user_input = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.ID, "username"))
        )
        ava_user_input.clear()
        ava_user_input.send_keys(Credentials.senai_user)
    
        # Password field
        ava_pass_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        ava_pass_input.clear()
        ava_pass_input.send_keys(Credentials.senai_password)
    
        # Click the login button (reliable for Brazilian Moodle instances)
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Entrar') or @id='loginbtn']"))
        )
        login_button.click()
    
        print("AVA SESI SENAI credentials sent and login button clicked successfully!")
        time.sleep(7)  # Allow dashboard and any policy screen to load
    
    except Exception as e:
        print("Failed to log into AVA SESI SENAI:", e)
        
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