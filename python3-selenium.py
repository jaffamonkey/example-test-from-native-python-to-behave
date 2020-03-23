import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://duckduckgo.com")
        searchField = driver.find_element_by_name("q")
        searchField.send_keys("TrumpKlon")
        searchButton = driver.find_element_by_css_selector("[name=btnI]")
        searchButton.click()
        self.assertIn("TrumpKlon", driver.title)
        assert "Donald Trump personality simulator in the world." in driver.page_source
        driver.get_screenshot_as_file("test_end_capture.png")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
