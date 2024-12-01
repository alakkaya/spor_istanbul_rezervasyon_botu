import os
from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

chromedriver_path = "/Users/ali/Desktop/PYTHON/spor_istanbul_rezervasyon_botu/chromedriver"

driver = webdriver.Chrome(service=Service(chromedriver_path))

driver.get("https://online.spor.istanbul/uyegiris")

WebDriverWait(driver, 10).until( 
    EC.presence_of_element_located((By.ID, "txtTCPasaport") )
)

# Kullanıcı İD ve şifreyi .env dosyasından al
id = os.getenv("SPOR_ISTANBUL_ID")
password = os.getenv("SPOR_ISTANBUL_PASSWORD")


#put the id and password
input_element = driver.find_element(By.ID, "txtTCPasaport")
input_element.clear()
input_element.send_keys(id)

input_element = driver.find_element(By.ID, "txtSifre")
input_element.clear()
input_element.send_keys(password)

WebDriverWait(driver, 5).until( 
    EC.presence_of_element_located((By.ID, "btnGirisYap") )
)
input_element = driver.find_element(By.ID, "btnGirisYap")
input_element.click()

# Giriş yaptıktan sonra sayfanın yüklenmesini bekleyin
WebDriverWait(driver, 20).until(
    EC.url_changes("https://online.spor.istanbul/uyegiris")
)

# Pop-up varsa kapat
try:
    pop_up = driver.find_element(By.ID, "modal")
    if pop_up:
        dont_show = driver.find_element(By.ID, "checkBox")
        dont_show.click()
        close_button = driver.find_element(By.ID, "closeModal")
        close_button.click()
except:
    pass

# Ana sayfanın tamamen yüklendiğinden emin olmak için belirli bir elemanın varlığını bekleyin
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "liseanslarim"))
)
seanslarım = driver.find_element(By.ID, "liseanslarim")
seanslarım.click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "pageContent_rptListe_lbtnSeansSecim_0"))
)
seans_sec = driver.find_element(By.ID, "pageContent_rptListe_lbtnSeansSecim_0")
seans_sec.click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "lbtnKaydet"))
)

# Bugünün tarihini al
# today = datetime.today().strftime('%d.%m.%Y')
today = "02.12.2024"

# Tarih ile eşleşen kolonu bul ve checkbox'ı seç
panels = driver.find_elements(By.CLASS_NAME, "panel-info")
for panel in panels:
    date_element = panel.find_element(By.CLASS_NAME, "panel-title")
    date_text = date_element.get_attribute('innerHTML').split('<br>')[1].strip()
    
    if today in date_text:
        checkbox = panel.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        checkbox.click()
        break

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "pageContent_txtCaptchaText"))
)

# Captcha'yı çöz
captcha_image = driver.find_element(By.ID, "pageContent_captchaImage")
captcha_image.screenshot("captcha.png")

# Ekran görüntüsünün alınıp alınmadığını kontrol edin
if os.path.exists("captcha.png"):
    print("Ekran görüntüsü başarıyla alındı.")
else:
    print("Ekran görüntüsü alınamadı.")

# Tesseract OCR kullanarak metni çıkarın
captcha_text = pytesseract.image_to_string(Image.open("captcha.png"))

# Çıkarılan metni yazdırarak kontrol edin
print("Captcha metni:", captcha_text)

captcha_input = driver.find_element(By.ID, "pageContent_txtCaptchaText")
captcha_input.send_keys(captcha_text)

# Kaydet butonuna tıkla 
# kaydet = driver.find_element(By.ID, "lbtnKaydet")
# kaydet.click()
# Tarayıcının kapanmasını engellemek için bekleme ekleyin
input("Devam etmek için Enter tuşuna basın...")

driver.quit()