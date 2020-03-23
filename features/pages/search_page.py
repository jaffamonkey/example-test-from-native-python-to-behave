from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage

class SearchPage(BasePage):
    BUTTON_SEARCH = (By.XPATH, "//button[@type='submit']")
    FIELD_SEARCH = (By.NAME, "q")

    def _verify_page(self):
        self.on_this_page(self.FIELD_SEARCH)
        
    def type_in_search_field(self, text):
        self.type_in(self.FIELD_SEARCH, text)

    def click_search(self):
        self.click_on(self.BUTTON_SEARCH)
