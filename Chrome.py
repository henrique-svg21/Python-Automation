from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#import credentials from another file for security measures
import Credentials

chrome_options = Options()

# Open in Incognito
chrome_options.add_argument("--incognito")

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

# 6. Navigate to the main Google page (Brazilian Portuguese)
browser.get("https://www.google.com/?hl=pt_BR")