import configparser
import os
# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    chrome_options.headless = True
    chrome_path = os.getcwd() + "/bin/chromedriver"
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    parser = configparser.ConfigParser()
    parser.read("behave.ini")
    context.config = parser

def before_scenario(context, scenario):
    context.driver.delete_all_cookies()

# def after_all(context):
#     context.driver.quit()
