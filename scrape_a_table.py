import pandas as pd
from mail import username
from password import password
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from get_gecko_driver import GetGeckoDriver

get_driver = GetGeckoDriver()
get_driver.install()
driver = webdriver.Firefox()


def site_login():
    driver.get(
        "https://elkv-dev6.fa.us6.oraclecloud.com/analytics/saw.dll?bipublisherEntry&Done=%2fanalytics%2fsaw.dll%3fAdmin&Action=admin"
    )
    driver.implicitly_wait(10)
    driver.find_element(by=By.CLASS_NAME, value="textInput").send_keys(username)
    driver.find_element(by=By.ID, value="password").send_keys(password)
    driver.find_element(by=By.CSS_SELECTOR, value="#btnActive").click()


site_login()


def navigate_to_table():
    driver.find_element(by=By.XPATH, value="//a[text()='FTP']").click()


navigate_to_table()
