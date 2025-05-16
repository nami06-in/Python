import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/angela/Development/chromedriver"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_USERNAME = os.environ["TWITTER_USERNAME"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:

    def __init__(self, chrome_driver_options):
        self.driver = webdriver.Chrome(options=chrome_driver_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()

        time.sleep(2)
        go_button = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        continue_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        continue_button.click()

        time.sleep(40)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"down: {self.down}")
        time.sleep(10)
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        self.driver.maximize_window()

        time.sleep(5)
        email_field = self.driver.find_element(By.NAME, "text")
        email_field.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        email_field.send_keys(Keys.ENTER)

        try:
            time.sleep(3)
            user_name_field = self.driver.find_element(By.NAME, "text")
            user_name_field.send_keys(TWITTER_USERNAME)
            time.sleep(2)
            user_name_field.send_keys(Keys.ENTER)
        except Exception as error:
            print(f"Exception ocured \n {error}")

        time.sleep(5)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password_field.send_keys(Keys.ENTER)

        time.sleep(5)
        try:
            close_symbol = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/button/div/svg')
            close_symbol.click()
        except Exception as error:
            print(f"Exception ocured \n {error}")

        tweet_field = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_field.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

        time.sleep(5)
        everyone_reply = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div/div/div/button/div/span/span')
        everyone_reply.click()

        time.sleep(3)
        accounts_i_follow = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/span')
        accounts_i_follow.click()

        time.sleep(3)
        post_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        post_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

bot = InternetSpeedTwitterBot(chrome_options)
bot.get_internet_speed()
time.sleep(2)
bot.tweet_at_provider()
