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
    category = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.xpaths['yetu_cat'])))
    category.click()
    event_types = []
    for x in driver.find_elements_by_class_name("BLM-categoryListItem"):
        temp = x.get_attribute('value')
        if temp not in event_types and temp != None:
            event_types.append(temp)
    return event_types



def get_events(driver,event_types,saved_tab):
    driver.switch_to.window(saved_tab)
    allEvents = {}
    for item in event_types:
        event_block = driver.find_element(By.XPATH, "//div[@value='"+item+"']")
        event_block.click()
        # Switch to over/under
        # over_under = event_block.find_element(By.CSS_SELECTOR, "[value='over_under']")
        over_under = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//li[.='Over/Under']")))
        over_under.click()
        # switch to over/under 2.5
        over_under_25 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='TG 2.5']")))
        over_under_25.click()
        leagues = {}
        for x in driver.find_elements(By.CSS_SELECTOR, ".BLM-leagueName"):
            temp = {}
            temp['name'] = str(x.text)
            events = []
            count = driver.find_elements(By.XPATH, "//div[@id='BLM-sports-topLeagues']/div[3]//div[@class='BLM-leagueBox-content']/div")
            print(f"\t\tcount = {len(count)}\n\n")
            y=3
            while (driver.find_element(By.XPATH, "//div[@id='BLM-sports-topLeagues']/div["+str(y)+"]//div[1]/div[@class='BLM-matchDetails-container']") != None):
                z = 1
                while(driver.find_element(By.XPATH, "//div[@id='BLM-sports-topLeagues']/div["+str(y)+"]//div[@class='BLM-leagueBox-content']/div[1]//div[@class='BLM-matchDetails']") != None):
                    event_str = ''
                    for part in range(1,3):
                        event = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='BLM-sports-topLeagues']/div["+str(y)+"]//div[@class='BLM-leagueBox-content']/div["+str(z)+"]//div[@class='BLM-matchDetails']/div/div/div["+str(part)+"]")))
                        event_str += str(event.text)
                        if part == 1:
                            event_str += ' vs '
                        text_str = "//div[@id = 'BLM-sports-topLeagues']/div["+str(y)+"]//div[@class = 'BLM-leagueBox-content']/div["+str(z)+"]//div[@class = 'BLM-matchDetails']/div/div/div["+str(part)+"]"
                        print(text_str)
                    events.append(event_str)
                    z+=1
                y+=1
            temp['events'] = events

        leagues[len(leagues)] = temp
        allEvents[len(allEvents)] = leagues
    return allEvents

