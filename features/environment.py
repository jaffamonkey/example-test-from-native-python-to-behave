import configparser
import os
# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    options = Options()
    options.headless = True
    CHROMEDRIVER_PATH = os.getcwd() + "/bin/chromedriver"
    context.driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    parser = configparser.ConfigParser()
    parser.read("behave.ini")
    context.config = parser

def before_scenario(context, scenario):
    context.driver.delete_all_cookies()

# def after_all(context):
#     context.driver.quit()
