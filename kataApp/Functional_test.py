from __future__ import absolute_import

import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
class FunctionalTest (TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome('/Users/abonil4/Downloads/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get('http://127.0.0.1:8000')
        print(self.browser.title)
        self.assertIn('prueba', self.browser.title)





