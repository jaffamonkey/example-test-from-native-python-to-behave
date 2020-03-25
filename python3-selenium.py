import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class PythonOrgSearch(unittest.TestCase):

    def test_search_in_python_org(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_driver = os.getcwd() + os.sep + "chromedriver"
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
        driver.get("https://duckduckgo.com")
        searchField = driver.find_element_by_name("q")
        searchField.send_keys("TrumpKlon")
        searchButton = driver.find_element_by_css_selector("[id=search_button_homepage]")
        searchButton.click()
        self.assertIn("TrumpKlon", driver.title)
        assert "Donald Trump personality simulator in the world." in driver.page_source
        driver.get_screenshot_as_file("test_end_capture.png")

if __name__ == "__main__":
    unittest.main()
    
