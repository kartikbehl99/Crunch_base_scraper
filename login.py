from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By


def login(wait, driver, user_name, password):
    wait.until(presence_of_element_located((By.ID, "mat-input-1")))
    wait.until(presence_of_element_located((By.ID, "mat-input-2")))

    driver.find_element_by_id("mat-input-1").send_keys(user_name)
    driver.find_element_by_id("mat-input-2").send_keys(password)

    login_button = driver.find_element_by_xpath(
        "//form[@class='ng-dirty ng-touched ng-valid']//button[@type='submit']")
    login_button.click()
