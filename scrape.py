from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from team import get_team_details
import time
import json


def scrape(company_name, wait, driver):
    wait.until(presence_of_element_located((By.XPATH, "//results")))

    header_xpath = "//results//sheet-grid//grid-header//grid-column-header[2]/div/div"
    wait.until(presence_of_element_located((By.XPATH, header_xpath)))

    header = driver.find_element_by_xpath(header_xpath)

    xpath = f"//results//sheet-grid//div[@class='grid-container']/grid-body//grid-row[1]//grid-cell[3]//a[1]"

    if header.text == "Organization/Person Name":
        xpath = f"//results//sheet-grid//div[@class='grid-container']/grid-body//grid-row[1]//grid-cell[2]//a[1]"

    try:
        wait.until(presence_of_element_located((By.XPATH, xpath)))
    except Exception:
        return None

    company_name_link = driver.find_element_by_xpath(xpath)
    company_name_txt = company_name_link.text

    if company_name_txt != company_name:
        driver.back()
        return None

    driver.execute_script("arguments[0].click();", company_name_link)
    time.sleep(5)
    team_details = get_team_details(wait, driver)

    driver.back()

    return team_details
