from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from member import get_member_details
import time


def get_team_details(wait, driver):
    wait.until(presence_of_element_located((By.XPATH, "//entity-section")))

    entity_sections = driver.find_elements_by_xpath(
        "//entity-switcher[@class='ng-star-inserted']/entity/page-layout/div[2]//entity-section")

    company_website = None
    try:
        company_website_xpath = f"//entity-switcher[@class='ng-star-inserted']/entity/page-layout/div[2]//entity-section[1]/section-layout/mat-card/div[2]/fields-card"
        all_cards = driver.find_elements_by_xpath(company_website_xpath)
        company_website_xpath = f"//entity-switcher[@class='ng-star-inserted']/entity/page-layout/div[2]//entity-section[1]/section-layout/mat-card/div[2]/fields-card[{len(all_cards)}]/div/span[2]/field-formatter/link-formatter/a"
        company_website = driver.find_element_by_xpath(
            company_website_xpath).get_attribute("href")
    except Exception as e:
        print(str(e))
        pass

    team_xpath = None
    it_spend_xpath = None
    for i in range(len(entity_sections)):
        try:
            xpath = f"//entity-switcher[@class='ng-star-inserted']/entity/page-layout/div[2]//entity-section[{i + 1}]//h2[1]"
            heading = driver.find_element_by_xpath(xpath)
            if str(heading.text).strip() == "IT Spend by Aberdeen":
                it_spend_xpath = f"//entity-switcher[@class='ng-star-inserted']/entity/page-layout/div[2]//entity-section[{i + 1}]"
            if(str(heading.text).strip() == "Current Team"):
                team_xpath = f"//entity-switcher[@class='ng-star-inserted']/entity/page-layout/div[2]//entity-section[{i + 1}]"
                break
        except Exception:
            continue

    if team_xpath == None or it_spend_xpath == None:
        return None

    team_xpath += "/section-layout/mat-card/div[2]/image-list-card/div[1]/div"
    it_spend_xpath += "/section-layout/mat-card/div[2]/phrase-list-card/field-formatter[2]/a"

    wait.until(presence_of_element_located((By.XPATH, it_spend_xpath)))

    it_spend = driver.find_element_by_xpath(it_spend_xpath).text

    team_members = driver.find_elements_by_xpath(team_xpath)
    team_xpath = team_xpath[:-4]

    data = dict()
    data["website"] = company_website
    data["IT spend"] = it_spend
    print(company_website)
    print(it_spend)

    for i in range(len(team_members)):
        try:
            member_xpath = f"{team_xpath}/div[{i + 1}]/div[1]/a"
            wait.until(presence_of_element_located(
                (By.XPATH, member_xpath)))

            element = driver.find_element_by_xpath(member_xpath)
            ActionChains(driver).move_to_element(element).perform()

            driver.execute_script("arguments[0].click();", element)

            time.sleep(4)

            member_name, member_details = get_member_details(wait, driver)
            if member_name != None:
                data[member_name] = member_details

            print(i)
            print(member_name)
            print(member_details)

            driver.back()
        except Exception:
            driver.back()

    return data
