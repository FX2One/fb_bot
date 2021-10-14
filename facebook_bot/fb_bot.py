from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *

class Fb_bot:
    def __init__(self,driver,url,username,password):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(driver, options = self.options)
        self.driver.get(url)
        self.accept_cookies()
        self.login(username, password)

    def accept_cookies(self):
        cookies = self.driver.find_element_by_xpath('//*[@title="Allow All Cookies"]')
        cookies.click()

    def login(self,username, password):
        email = self.driver.find_element_by_id('email')
        email.send_keys(username)

        pass_input = self.driver.find_element_by_id('pass')
        pass_input.send_keys(password)

        login_btn = self.driver.find_element_by_name('login')
        login_btn.click()




