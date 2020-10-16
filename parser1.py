from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

from item import myItem


def search_item(item):
    path = "C:/Users/Noam/PycharmProjects/pythonProject/venv/Lib/site-packages/chromedriver_binary/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.yad2.co.il/products/all")
    try:
        search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "info")))
    except TimeoutException:
        search = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.NAME, "info")))

    search.send_keys(item.name)
    search.send_keys(Keys.RETURN)
    try:
        price = WebDriverWait(driver, 10, 1).until(
            expect.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='עד מחיר']")))

        price.send_keys(str(item.max_price))

        price.send_keys(Keys.RETURN)
        filter_button = driver.find_element_by_class_name("y2_btn.filter_btn")
        filter_button.click()
        items_list = []
        try:
            price.send_keys(Keys.RETURN)
            # items = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "feed_list")))
            i = 0
            while True:
                try:
                    item_id = "feed_item_" + str(i)
                    item = driver.find_element_by_id(item_id)
                    try:
                        updated_today = "עודכן היום"
                        if updated_today in item.text:
                            items_list.append(item.text)
                            notify = 1
                            i += 1
                        else:
                            break
                    except StaleElementReferenceException:
                        break
                except NoSuchElementException:
                    break
        except TimeoutException:
            price = WebDriverWait(driver, 100, 1).until(
                expect.visibility_of_element_located(
                    (By.XPATH, "//input[@placeholder='עד מחיר']")))
        time.sleep(5)
        driver.quit()
        return items_list

    except TimeoutException:
        driver.quit()





