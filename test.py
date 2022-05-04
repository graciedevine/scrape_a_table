from selenium import webdriver
from get_gecko_driver import GetGeckoDriver

get_driver = GetGeckoDriver()
get_driver.install()
driver = webdriver.Firefox()

driver.get(
    "https://elkv-dev6.fa.us6.oraclecloud.com/analytics/saw.dll?bipublisherEntry&Done=%2fanalytics%2fsaw.dll%3fAdmin&Action=admin"
)
