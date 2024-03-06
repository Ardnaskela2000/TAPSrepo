import unittest
from selenium import webdriver
from time import sleep


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://fabrykatestow.pl'
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        title = self.driver.title
        print('Tytuł strony: ' + title)

    def test2(self):
        source = self.driver.page_source
        print(source)

    def test3(self):
        current_url = self.driver.current_url
        print(current_url)


