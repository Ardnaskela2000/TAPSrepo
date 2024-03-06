from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# ustalenie strony WWW
url = 'https://google.pl'
driver.get(url)

# klikniecie button "Zaakceptuj wszystko"
accept_box = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
accept_box.click()

# wyszukanie w wyszukiwarce hasła
search_box = driver.find_element('name', 'q')
search_box.send_keys('selenium python')
search_box.submit()



time.sleep(5)

driver.quit()
