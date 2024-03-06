import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://simpletestsite.fabrykatestow.pl/'
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="checkbox-header"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').click()
        sleep(1)
        self.driver.save_screenshot('shot.png')
        sleep(1)





# //*[@id="checkbox-header"]