from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Import your custom credentials file
import Credentials

# 1. Set up Chrome Options
chrome_options = Options()

# Open in Incognito ("Navegação Anônima")
chrome_options.add_argument("--incognito")

# Keep the browser open after the script finishes
chrome_options.add_experimental_option("detach", True)

# Hide basic automation banners to help avoid detection
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

servicce = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servicce, options=chrome_options)

# 2. Go directly to the Google Login page
browser.get("https://accounts.google.com/")

# 3. Wait for the VISIBLE email field, type email, and press Enter
email_input = WebDriverWait(browser, 30).until(
    EC.visibility_of_element_located((By.ID, "identifierId"))
)
email_input.send_keys(Credentials.email + Keys.ENTER)

# 4. Wait for the VISIBLE password field to appear. 
# We use visibility_of_element_located and XPATH to ignore Google's hidden trap boxes.
password_input = WebDriverWait(browser, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
)

# Wait just 1 second for the sliding animation to completely settle focus
time.sleep(1)

# Now type the password and press Enter
password_input.send_keys(Credentials.password + Keys.ENTER)

# 5. Give Google 5 seconds to process the login
time.sleep(5)

# 6. Navigate to the main Google page (Brazilian Portuguese)
browser.get("https://www.google.com/?hl=pt_BR")