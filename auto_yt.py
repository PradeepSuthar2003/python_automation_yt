import webbrowser as web
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--lang-en")
browser = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(), options=options)
browser.get("https://www.youtube.com")

time.sleep(5)

user = browser.find_element(By.CSS_SELECTOR, "input[name='search_query']")
user.send_keys("alan walker")
btn = browser.find_element(By.XPATH, "//button[@id='search-icon-legacy']")
btn.click()
time.sleep(3)
vdo = browser.find_element(
    By.CLASS_NAME, "style-scope ytd-item-section-renderer")
vdo.click()

time.sleep(8)

try:
    skip = browser.find_element(
        By.XPATH, "//button[@class='ytp-ad-skip-button ytp-button']")
    skip.click()
except:
    print("ad note found")

browser.fullscreen_window()
time.sleep(200)
# style-scope ytd-item-section-renderer
