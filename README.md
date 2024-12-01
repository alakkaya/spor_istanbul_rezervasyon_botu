# Spor Istanbul Rezervasyon Botu

Bu proje, Spor Istanbul web sitesine otomatik giriş yaparak rezervasyon işlemlerini gerçekleştiren bir Selenium botudur.

## Başlarken

Bu talimatlar, projenin yerel makinenizde nasıl çalıştırılacağını açıklamaktadır.

### Gereksinimler

- Python 3.x
- Selenium
- python-dotenv
- Google Chrome
- ChromeDriver
- Tesseract OCR (Captcha çözümü için)

### Kurulum

1. Bu projeyi yerel makinenize klonlayın:

    ```sh
    git clone https://github.com/kullaniciadi/spor-istanbul-rezervasyon-botu.git
    cd spor-istanbul-rezervasyon-botu
    ```

2. Gerekli Python paketlerini yükleyin:

    ```sh
    pip install selenium python-dotenv pytesseract pillow
    ```

3. ChromeDriver'ı indirin ve projenizin kök dizinine yerleştirin. ChromeDriver'ı [buradan](https://sites.google.com/a/chromium.org/chromedriver/downloads) indirebilirsiniz.

4. Tesseract OCR'ı indirin ve kurun. Kurulum talimatları için [buraya](https://github.com/tesseract-ocr/tesseract) bakabilirsiniz.

5. `.env` dosyasını oluşturun ve aşağıdaki gibi doldurun:

    ```properties
    SPOR_ISTANBUL_ID=Tc Kimlik No
    SPOR_ISTANBUL_PASSWORD=Şifre
    ```

### Kullanım

1. `main.py` dosyasını çalıştırın:

    ```sh
    python main.py
    ```

2. Bot, Spor Istanbul web sitesine giriş yapacak ve rezervasyon işlemlerini gerçekleştirecektir.

### Kod Açıklaması

- `main.py`: Botun ana çalışma dosyasıdır. Selenium kullanarak web sitesine giriş yapar ve captcha dışındaki rezervasyon işlemlerini gerçekleştirir.
- `.env`: Kullanıcı kimlik bilgilerini içerir.

#### `main.py` Dosyası

- `.env` dosyasını yükler ve kullanıcı kimlik bilgilerini alır.
- ChromeDriver'ı başlatır ve Spor Istanbul giriş sayfasına gider.
- Kullanıcı kimlik bilgilerini girer ve giriş yapar.
- Giriş yaptıktan sonra, belirli bir sayfanın yüklenmesini bekler ve rezervasyon işlemlerini gerçekleştirir.
- Captcha çözümü için Tesseract OCR kullanır.

