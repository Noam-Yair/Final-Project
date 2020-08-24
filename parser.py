from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def searchItem(item, maxPrice):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.yad2.co.il/products/all")

    try:
        search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "info")))
    except TimeoutException:
        print("")

    search.send_keys(item)
    search.send_keys(Keys.RETURN)

    price = WebDriverWait(driver, 20, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='עד -']")))
    price.send_keys(str(maxPrice))
    price.send_keys(Keys.RETURN)

    time.sleep(10)
    driver.quit()