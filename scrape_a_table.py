import pandas as pd
from mail import username
from password import password
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from get_gecko_driver import GetGeckoDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

get_driver = GetGeckoDriver()
get_driver.install()
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)


def site_login():
    driver.get(
        "https://elkv-dev6.fa.us6.oraclecloud.com/analytics/saw.dll?bipublisherEntry&Done=%2fanalytics%2fsaw.dll%3fAdmin&Action=admin"
    )
    driver.implicitly_wait(10)
    driver.find_element(by=By.CLASS_NAME, value="textInput").send_keys(username)
    driver.find_element(by=By.ID, value="password").send_keys(password)
    driver.find_element(by=By.ID, value="ssoBtn").click()


def mfa():
    wait.until(EC.element_to_be_clickable((By.ID, "i0116"))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "i0118"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
    driver.execute_script("window.history.go(-1)")


def navigate_to_table():
    super_wait = WebDriverWait(driver, 30)
    super_wait.until(EC.element_to_be_clickable((By.ID, "labelDelivery"))).click()


# def find_table():
#     soup = BeautifulSoup(driver.page_source, "lxml")
#     tables = soup.find_all("table")
#     print(len(tables))
#     return tables


# def scrape_table(tables):
#     dfs = pd.read_html(str(tables))
#     print(f"Total tables: {len(dfs)}")
#     print(dfs[0])


site_login()
mfa()
navigate_to_table()
# find_table()
# scrape_table(find_table())
