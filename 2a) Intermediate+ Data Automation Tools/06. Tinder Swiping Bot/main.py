import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_EMAIL = os.environ["TINDER_ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["TINDER_ACCOUNT_PASSWORD"]

chrome_options = webdriver.ChromeOptions()  # To get hold of chrome options
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")
driver.maximize_window()

time.sleep(2)
accept_button = driver.find_element(By.XPATH, value='//*[@id="t-342688478"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_button.click()

time.sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="t-342688478"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(3)
try:
    login_with_FB = driver.find_element(By.XPATH, '//*[@id="t-2071069554"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
    login_with_FB.click()

except:
    more_option_button = driver.find_element(By.XPATH, '//*[@id="t-2071069554"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/button')
    more_option_button.click()
    time.sleep(5)
    login_with_FB = driver.find_element(By.XPATH,'//*[@id="t-2071069554"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
    login_with_FB.click()


time.sleep(2)
window_list = driver.window_handles
print(window_list)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

time.sleep(3)
email_field = driver.find_element(By.ID, "email")
email_field.send_keys(ACCOUNT_EMAIL)

time.sleep(3)
password_field = driver.find_element(By.ID, "pass")
password_field.send_keys(ACCOUNT_PASSWORD)
time.sleep(2)
password_field.send_keys(Keys.ENTER)

time.sleep(8)
continue_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span')
continue_button.click()

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(8)
location_popup = driver.find_element(By.XPATH, '//*[@id="t-2071069554"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]/div')
location_popup.click()

time.sleep(3)
notification_popup = driver.find_element(By.XPATH, '//*[@id="t-2071069554"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]/div')
notification_popup.click()

for n in range(100):
    try:
        time.sleep(2)
        dislike_button = driver.find_element(By.XPATH, '//button[contains(@Class, "gamepad-button") and .//span[contains(text(), "Nope")]]')
        dislike_button.click()
    except Exception as error:
        not_interested_button = driver.find_element(By.XPATH, '//button[.//div[text()="Not interested"]]')
        not_interested_button.click()
        continue

driver.quit()
