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


# def navigate_to_table():
#     print(f"{datetime.now()} Going to wait")
#     element = driver.find_element(by=By.XPATH, value="//a[text()='FTP']")
#     element = driver.find_element_by_xpath("//a[text()='FTP']")
#     print(element)
#     element.click()
#     function getx(s) { return document.evaluate(s, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue}


def find_table():
    driver.get(
        "https://elkv-dev6.fa.us6.oraclecloud.com/analytics/saw.dll?bipublisherEntry"
    )
    soup = BeautifulSoup(driver.page_source, "lxml")
    tables = soup.find_all("table")
    print(len(tables))

    # def scrape_table():
    #     dfs = pd.read_html(str(tables))
    #     print(f"Total tables: {len(dfs)}")
    #     print(dfs[0])
    #     driver.close()

 

    if __name__ == "__main__":
        site_login()
        # navigate_to_table()
        find_table()
        # scrape_table()

