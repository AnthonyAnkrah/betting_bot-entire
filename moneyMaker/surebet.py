# Import dependencies
from selenium import webdriver
import variables as var
import yetu
import sporty
import melbet
from pprint import pprint

# Create new instance of webdriver
driver = webdriver.Chrome(var.driver_path)
driver.maximize_window()

# Loop through available sites and get events
for index, item in enumerate(var.sites.keys()):
    if item == 'yetu':
        var.events[item] = yetu.scrape_event_type(driver, var.sites[item])
    elif item == 'mel':
        var.events[item] = melbet.scrape_event_type(driver, var.sites[item])
    elif item == 'sporty':
        var.events[item] = sporty.scrape_event_type(driver, var.sites[item])
    else:
        print(f'Unknown site index {item}')

    # Check if tab for site saved in tabs
    if item not in var.tabs.keys():
        var.tabs[item] = driver.window_handles[index]
    if index < len(var.sites)-1:
        # Open new tab
        driver.execute_script("window.open('')")
        driver.switch_to.window(driver.window_handles[index+1])


pprint(yetu.get_events(driver,var.events['yetu'],var.tabs['yetu']))

# Close the browser
driver.quit()
