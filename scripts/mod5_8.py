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
        self.driver.minimize_window()
        sleep(2)

    def test2(self):
        self.driver.set_window_size(800, 600)
        sleep(2)

    def test3(self):
        self.driver.set_window_position(500, 500)
        sleep(2)

