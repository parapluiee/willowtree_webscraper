from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
import time
cards = []

driver.get("https://www.harristeeter.com/pl/all/00?fulfillment=all?page=1")
time.sleep(5)
prices = driver.find_elements(By.XPATH, "//div[@class='kds-Card ProductCard border border-neutral-less-subtle border-solid flex flex-col w-full overflow-hidden px-8 pb-16 rounded-large hover:shadow-2']//data")
names = driver.find_elements(By.XPATH,  "//div[@class='kds-Card ProductCard border border-neutral-less-subtle border-solid flex flex-col w-full overflow-hidden px-8 pb-16 rounded-large hover:shadow-2']//h3[@data-qa='cart-page-item-description']")
l = len(prices)
print(len(prices))
print(len(names))
for i in range(l):
    print(prices[i].get_attribute("value") + " " + names[i].text)
    