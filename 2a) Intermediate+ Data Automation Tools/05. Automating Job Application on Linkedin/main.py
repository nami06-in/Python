import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv()

chrome_options = webdriver.ChromeOptions()  # To get hold of chrome options
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


def start():
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
               "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

    driver.maximize_window()
    time.sleep(3)

    try:
        sign_in = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div'
                                                      '/div/div[2]/button')

        sign_in.click()
        time.sleep(1)

        email = driver.find_element(By.NAME, "session_key")
        time.sleep(3)
        email.click()
        email.send_keys(os.environ["MY_EMAIL"])

        password = driver.find_element(By.NAME, "session_password")
        time.sleep(2)
        password.click()
        password.send_keys(os.environ["LINKEDIN_PASSWORD"])

        password.send_keys(Keys.ENTER)

        time.sleep(5)
        job_list = driver.find_elements(By.CSS_SELECTOR, ".ember-view a")
        print(len(job_list))

        for job_link in job_list:
            try:
                # job_link = driver.find_element(By.XPATH, f'/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{job_id}]/div/div/div[1]/div/div[2]/div[1]/a')
                job_link.click()
                time.sleep(1)
                save_button = driver.find_element(By.XPATH,
                                                  value='/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]'
                                                        '/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/'
                                                        'button')

                save_button.click()
                time.sleep(1)

            except Exception as error:
                print("An exception occurred:", error)
    except Exception as error:
        print("An exception occurred:", error)
        start()


start()
# '/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[1]/div/div/div[1]/div[1]/div[2]/div[1]/a'
# f'/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{}]/div/div/div[1]/div/div[2]/div[1]/a'
# '/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[3]/div/div/div[1]/div/div[2]/div[1]/a'
