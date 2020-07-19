from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
import time


def search_company(company_name, driver, wait):
    wait.until(presence_of_element_located(
        (By.XPATH, "//form[@class='component--multi-search ng-untouched ng-pristine ng-valid']//input[1]")))
    search_field = driver.find_element_by_xpath(
        "//form[@class='component--multi-search ng-untouched ng-pristine ng-valid']//input[1]")
    search_field.clear()
    search_field.send_keys(company_name)
    time.sleep(0.1)
    search_field.send_keys(Keys.ENTER)
