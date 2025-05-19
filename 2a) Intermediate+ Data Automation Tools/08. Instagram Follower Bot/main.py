import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv()

SIMILAR_ACCOUNT = os.environ["INSTAGRAM_SIMILAR_ACCOUNT"]
USERNAME = os.environ["INSTAGRAM_USERNAME"]
PASSWORD = os.environ["INSTAGRAM_PASSWORD"]


class InstaFollower:

    def __init__(self, chrome_driver_options):
        self.scrollable_popup = ""
        self.driver = webdriver.Chrome(options=chrome_driver_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()

        time.sleep(5)
        username_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(USERNAME)

        time.sleep(3)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(PASSWORD)

        time.sleep(3)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        time.sleep(8)
        save_info_button = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        save_info_button.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        time.sleep(7)
        followers_button = self.driver.find_element(by=By.XPATH, value="//a[contains(text(), ' followers')]")
        followers_button.click()

        time.sleep(7)
        self.scrollable_popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.scrollable_popup)
            time.sleep(8)

    def follow(self):
        self.driver.execute_script("arguments[0].scrollTop = 0", self.scrollable_popup)
        time.sleep(3)
        follow_buttons = self.driver.find_elements(by=By.XPATH, value="//div[contains(text(), 'Follow')]")
        print(follow_buttons)
        print(follow_buttons[0].text)
        time.sleep(5)
        for follow in follow_buttons:
            try:
                follow.click()
                time.sleep(3)

            except:
                pass


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

bot = InstaFollower(chrome_options)

bot.login()
time.sleep(5)
bot.find_followers()
bot.follow()