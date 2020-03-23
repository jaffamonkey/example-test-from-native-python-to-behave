from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() + os.sep + "chromedriver"

# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
driver.get("https://duckduckgo.com")
searchField = driver.find_element_by_name("q")
searchField.send_keys("TrumpKlon")
searchButton = driver.find_element_by_css_selector("[id=search_button_homepage]")
searchButton.click()
assert "TrumpKlon" in driver.title
assert "Donald Trump personality simulator in the world." in driver.page_source
# capture the screen
driver.get_screenshot_as_file("headless_test_end_capture.png")
