from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By


def get_member_details(wait, driver):
    wait.until(presence_of_element_located(
        (By.XPATH, "//entity-switcher/entity")))

    total_field_cards = driver.find_elements_by_xpath(
        "//entity-switcher/entity/page-layout/div[2]//entity-section[1]//fields-card")

    xpath_link_name = f"//entity-switcher/entity/page-layout/div[2]//entity-section[1]//fields-card[{len(total_field_cards)}]/div/span"

    try:
        wait.until(presence_of_element_located(
            (By.XPATH, "//entity-switcher/entity/page-layout/div[2]//entity-section[1]//image-with-fields-card/image-with-text-card/div/div/div[2]//span")))
        wait.until(presence_of_element_located((By.XPATH, xpath_link_name)))

        available_links = driver.find_elements_by_xpath(xpath_link_name)
        member_name = driver.find_element_by_xpath(
            "//entity-switcher/entity/page-layout/div[2]//entity-section[1]//image-with-fields-card/image-with-text-card/div/div/div[2]//span").text
        member_title = driver.find_element_by_xpath(
            "//entity-switcher/entity/page-layout/div[2]//entity-section[1]//image-with-fields-card/image-with-text-card/div/div/div[2]/div[2]//span"
        )
    except Exception:
        return None, None

    member_details = dict()
    member_details["title"] = member_title.text

    for i in range(0, len(available_links), 2):
        try:
            xpath_name = f"//entity-switcher/entity/page-layout/div[2]//entity-section[1]//fields-card[{len(total_field_cards)}]/div/span[{i + 1}]//span/span[2]/span"
            xpath_link = f"//entity-switcher/entity/page-layout/div[2]//entity-section[1]//fields-card[{len(total_field_cards)}]/div/span[{i + 2}]/field-formatter/link-formatter/a"
            # wait.until(presence_of_element_located((By.XPATH, xpath_name)))
            link_name = available_links[i].find_element_by_xpath(xpath_name)
            link = driver.find_element_by_xpath(
                xpath_link).get_attribute("href")

            member_details[link_name.text] = link
        except Exception:
            continue

    return member_name, member_details
