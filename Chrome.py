from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

#import credentials from another file for security measures
import Credentials

chrome_options = Options()

# Open in Incognito
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--force-dark-mode")
chrome_options.add_argument("--enable-features=WebUIDarkMode")

chrome_options.add_experimental_option("detach", True)

# Hide basic automation banners to help avoid detection
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

servicce = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servicce, options=chrome_options)

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

# Open a new blank tab
browser.execute_script("window.open('');")

# Switch Selenium's focus to that new tab (it's the second tab, so index is 1)
browser.switch_to.window(browser.window_handles[1])

# Navigate to Gemini
browser.get("https://gemini.google.com/app")

# Wait until the URL actually contains 'gemini' to ensure it loaded
WebDriverWait(browser, 10).until(
    EC.url_contains("gemini.google.com")
)

# A small buffer to let the UI and chat box fully render
time.sleep(3) 

print("Successfully opened Gemini!")

# ==========================================
# 3. GITHUB LOGIN (Standard User/Pass)
# ==========================================

# Open a third blank tab and switch to it (Index 2)
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[2])

# Go straight to GitHub's login page
browser.get("https://github.com/login")
print("Navigated to GitHub login page...")

try:
    # 1. Wait for the username/email field and type the credential
    github_user_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "login_field"))
    )
    github_user_input.send_keys(Credentials.github_email)

    # 2. Find the password field, type it, and hit ENTER to submit
    github_pass_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    # Using Keys.ENTER on the password field submits the form
    github_pass_input.send_keys(Credentials.github_password + Keys.ENTER)
    print("Sent GitHub credentials!")

except Exception as e:
    print("Failed to find GitHub login fields.", e)

# 3. Wait to ensure we successfully landed on the GitHub dashboard
try:
    # GitHub's dashboard URL is exactly "https://github.com/" after logging in
    WebDriverWait(browser, 15).until(
        EC.url_to_be("https://github.com/")
    )
    print("Successfully logged into GitHub!")
except:
    print("Login might have failed, or we hit a 2FA/Device Verification screen. Check the browser.")

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[3])
browser.get("https://www.google.com")