from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.support.ui import Select

class Fb_bot_register:
    def __init__(self,driver,url,firstName,lastName,randMail):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(driver, options = self.options)
        self.driver.get(url)
        self.accept_cookies()
        self.create_account()
        time.sleep(5)
        self.fill_form(firstName,lastName,randMail)


    def accept_cookies(self):
        cookies = self.driver.find_element_by_xpath('//*[@title="Allow All Cookies"]')
        cookies.click()

    def create_account(self):
        ca = self.driver.find_element_by_xpath('//*[@data-testid="open-registration-form-button"]')
        ca.click()

    def fill_form(self, firstName,lastName,randMail):
        first_name = self.driver.find_element_by_name('firstname')
        first_name.send_keys(firstName)

        last_name = self.driver.find_element_by_name('lastname')
        last_name.send_keys(lastName)

        email = self.driver.find_element_by_name('reg_email__')
        email.send_keys(randMail)

        password = self.driver.find_element_by_name('reg_passwd__')
        password.send_keys('SomeRandomPassword')

        re_mail = self.driver.find_element_by_name('reg_email_confirmation__')
        re_mail.send_keys(randMail)

        month = self.driver.find_element_by_name('birthday_month')
        monthDD = Select(month)
        monthDD.select_by_index(random.randrange(11))

        day = self.driver.find_element_by_name('birthday_day')
        dayDD = Select(day)
        dayDD.select_by_index(random.randrange(27))

        year = self.driver.find_element_by_name('birthday_year')
        yearDD = Select(year)
        yearDD.select_by_index(random.randint(20,50))

        gender = self.driver.find_element_by_xpath('//label[text()="Male"]')
        gender.click()

        '''sign = self.driver.find_element_by_xpath('//button[text()="Sign Up"]')
        sign.click()'''
        













