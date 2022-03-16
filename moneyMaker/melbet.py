# Import dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import variables as var


# Scrape site for all event types
# Args (driver, url)
# Args: driver - An instance of the webdriver class to interact with the browser (Object)
# Args: url - The URL of the site to be scraped (String)
#
# Returns: event_types - A list of event types on site (list)
def scrape_event_type(driver, url):
    driver.get(url)
    category = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, var.xpaths['mel_cat'])))
    category.click()
    event_types = []
    for x in driver.find_elements_by_xpath(".//a[@class='link sportMenu']/span[@class='name']"):
        if str(x.text) not in event_types:
            event_types.append(str(x.text))
    return event_types
