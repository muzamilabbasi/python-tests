from util import mouseactions
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time, re, datetime

class MoneyMediaPubTestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://stage-rams.cosmopolitan.com")
        return self.driver
        
    def tearDown(self):
        return self.driver.quit()
