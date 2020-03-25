from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from features.pages.search_page import SearchPage

@when('I click element with text "{text}"')
def step_impl(context, text):
    element = (By.XPATH, "//*[text() = '{}']".format(text))
    WebDriverWait(context.driver, 10).until(ec.element_to_be_clickable(element), "Unable to click element").click()

@then('I see element with text "{text}"')
def step_impl(context, text):
    element = (By.TAG_NAME, "body")
    WebDriverWait(context.driver, 10).until(ec.text_to_be_present_in_element(element, text), "Unable to find text")

@given("I open search page")
def step_impl(context):
    context.driver.get("https://duckduckgo.com")

@when('I type "{searchstring}" in search field')
def step_impl(context, searchstring):
    search_page = SearchPage(context.driver)
    search_page.type_in_search_field(searchstring)

@when("I click search button")
def step_impl(context):
    search_page = SearchPage(context.driver)
    search_page.click_search()
