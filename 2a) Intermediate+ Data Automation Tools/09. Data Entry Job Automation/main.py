import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

"""
    1. Go to https://docs.google.com/forms/ and create your own form.

    2. Add 3 questions to the form, make all questions "short-answer":
       q) What's the address of the property?
       q) What's the price per month?
       q) What's the link to the property?
"""

GOOGLE_FORM_LINK = os.environ["GOOGLE_FORM_LINK"]
FORM_RESPONSE_LINK = os.environ["FORM_RESPONSE_LINK"]
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"

RESPONSE = requests.get(ZILLOW_LINK)
CONTENTS = RESPONSE.text

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("detach", True)


class DataEntry:
    def __init__(self):
        self.soup = BeautifulSoup(CONTENTS, "html.parser")
        self.driver = webdriver.Chrome(options=CHROME_OPTIONS)
        self.link_list = []
        self.address_list = []
        self.price_list = []

    def get_data(self):
        anchor_tag = self.soup.find_all(name="a", class_="property-card-link")
        self.link_list = [element.get('href') for element in anchor_tag]
        print(self.link_list)

        price_tag = self.soup.find_all(name="div", class_="PropertyCardWrapper")
        self.price_list = [element.get_text().strip("\n").split("+")[0].replace("/mo", "") for element in price_tag]
        print(self.price_list)

        address_tag = self.soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
        self.address_list = [element.get_text().strip("\n'  '") for element in address_tag]
        print(self.address_list)

    def make_form(self):
        for data in range(len(self.address_list)):
            self.driver.get(GOOGLE_FORM_LINK)
            self.driver.maximize_window()

            time.sleep(5)

            address_field = self.driver.find_element(By.XPATH,
                                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_field.send_keys(self.address_list[data])

            time.sleep(1.1)
            price_field = self.driver.find_element(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field.send_keys(self.price_list[data])

            time.sleep(1.1)
            link_field = self.driver.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field.send_keys(self.link_list[data])

            time.sleep(1.5)
            submit_field = self.driver.find_element(By.XPATH,
                                               '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit_field.click()

            time.sleep(3)


bot = DataEntry()
bot.get_data()
bot.make_form()

