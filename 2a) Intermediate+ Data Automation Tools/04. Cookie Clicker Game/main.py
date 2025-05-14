import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()  # To get hold of chrome options
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

timeout = time.time() + 60*5  # 5-minute timeout
start_time = time.time()  # Track the starting time


while True:
    cookie.click()
    cookie.click()
    cookie.click()

    if time.time() > timeout:
        break

    if int(time.time() - start_time) % 5 == 0:  # Every 5 seconds
        auto_cursor_cost_text = driver.find_element(By.CSS_SELECTOR, '#buyCursor b').text
        auto_cursor_cost = int(auto_cursor_cost_text.split()[2].replace(",", ""))

        grandma_cost_text = driver.find_element(By.CSS_SELECTOR, '#buyGrandma b').text
        grandma_cost = int(grandma_cost_text.split()[2].replace(",", ""))

        factory_cost_text = driver.find_element(By.CSS_SELECTOR, '#buyFactory b').text
        factory_cost = int(factory_cost_text.split()[2].replace(",", ""))

        mine_cost_text = driver.find_element(By.CSS_SELECTOR, '#buyMine b').text
        mine_cost = int(mine_cost_text.split()[2].replace(",", ""))

        my_money = int(driver.find_element(By.ID, 'money').text)

        if my_money >= mine_cost <= factory_cost:
            cursor = driver.find_element(By.ID, value="buyMine")
            cursor.click()

        elif my_money >= factory_cost <= grandma_cost:
            cursor = driver.find_element(By.ID, value="buyFactory")
            cursor.click()

        elif my_money >= grandma_cost <= auto_cursor_cost:
            cursor = driver.find_element(By.ID, value="buyGrandma")
            cursor.click()

        elif my_money >= auto_cursor_cost:
            cursor = driver.find_element(By.ID, value="buyCursor")
            cursor.click()

    # time.sleep(0.000000000000000000001)  # Sleep for 1 second each iteration


cookie_per_second = driver.find_element(By.ID, value="cps").text
print(cookie_per_second.split(":")[1])
driver.quit()
