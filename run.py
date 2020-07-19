from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import json
import time
from login import login
from search_compay import search_company
from scrape import scrape

with open("./config.json") as json_file:
    data = json.load(json_file)
    user_name = data["credentials"]["userName"]
    password = data["credentials"]["password"]

with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 50)
    driver.maximize_window()

    driver.get("https://www.crunchbase.com/login")

    login(wait, driver, user_name, password)
    time.sleep(5)

    with open("./companies.json", "r") as json_file:
        companies = json.load(json_file)["companies"]

    data_file = open("data.json", "w")
    data = dict()

    for company_name in companies:
        search_company(company_name, driver, wait)
        time.sleep(2)
        details = scrape(company_name, wait, driver)
        if details == None:
            continue
        data[company_name] = details
        data_file.seek(0)
        data_file.write(json.dumps(data))
    # time.sleep(100)

    # driver.back()
