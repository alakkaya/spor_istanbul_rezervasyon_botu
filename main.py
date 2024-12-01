from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = "/Users/ali/Desktop/PYTHON/spor_istanbul_rezervasyon_botu/chromedriver"

driver = webdriver.Chrome(service=Service(chromedriver_path))

driver.get("https://www.spor.istanbul/")



time.sleep(10);

driver.quit()