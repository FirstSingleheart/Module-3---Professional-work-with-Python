from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Opera()
driver.get("https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fpassport.yandex.ru%2Fprofile&noreturn=1")
assert "Авторизация" in driver.title
elem = driver.find_element_by_name("login")
time.sleep(2)
elem.send_keys("pycon")
time.sleep(2)
elem.send_keys(Keys.RETURN)
time.sleep(2)
assert "No results found." not in driver.page_source
driver.close()
driver.quit()