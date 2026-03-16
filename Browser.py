from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

servicee = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service = servicee)

try:
    browser.get("https://www.google.com")

    search = browser.find_element(By.NAME, "q")
    search.send_keys("Senai Automação" + Keys.ENTER)

    time.sleep(5)

finally:
    browser.quit()