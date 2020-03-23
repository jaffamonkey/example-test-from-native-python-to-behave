from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchPage(BasePage):
    BUTTON_LOGIN = (By.XPATH, "//button[@type='submit']")
    FIELD_SEARCH = (By.XPATH, "//input[@placeholder = 'Search']")

    def _verify_page(self):
        self.on_this_page(self.FIELD_SEARCH)
        
    def type_in_search_field(self, text):
        self.type_in(self.FIELD_SEARCH, text)


    def _verify_page(self):
        self.on_this_page(self.FIELD_USERNAME, self.FIELD_PASSWORD)

    def enter_username(self, username):
        self.type_in(self.FIELD_USERNAME, username)

    def enter_password(self, password):
        self.type_in(self.FIELD_PASSWORD, password)

    def click_search(self):
        self.click_on(self.BUTTON_LOGIN)
