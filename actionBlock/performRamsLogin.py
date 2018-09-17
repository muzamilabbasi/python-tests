from selenium import webdriver
import unittest
import urllib2

class performRamsLogin(unittest.TestCase):
    
    def __init__(self, driver):
        self.driver = driver
    
    def login(self):
        driver = webdriver.Firefox()
        driver.get("")
        username = driver.find_element_by_id("username")
        username.clear()
        username.send_keys("mabassi")
        password = driver.find_element_by_id("password")
        password.clear()
        password.send_keys("123456")
        loginButton = driver.find_element_by_xpath("//*[@id='contents']/form/div/p[4]/button")
        loginButton.click()
        articles = driver.find_element_by_xpath("//*[@id='header']/div[3]/ul/li[1]/a")
        articles.click()
        driver.find_element_by_id("id").send_keys("38590")
        driver.find_element_by_css_selector("#results_table > table > tbody > tr > td:nth-child(3) > a").click()
        driver.find_element_by_xpath("//*[@id='body_box']/div[2]/div/div[2]/div[3]/div[1]/span").click()
        driver.find_element_by_xpath("//*[@id='body_box']/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/textarea").send_keys("This is a test")
        driver.find_element_by_xpath("//*[@id='body_box']/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div/button").click()
    