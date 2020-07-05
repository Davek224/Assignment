import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "PythonAutomationFramework_1-master"))
from pages.LoginPage import locators
import selenium
from selenium.webdriver.common.by import By
from pages.LoginPage.widgets.LoginWidget.mainWidget import *
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*Main.username_textbox).clear()
        self.driver.find_element(*Main.username_textbox).send_keys(username)

    def enter_instance(self,instace):
        self.driver.find_element(*Main.instance_textbox).clear()
        self.driver.find_element(*Main.instance_textbox).send_keys(instace)

    def enter_password(self, password):
        self.driver.find_element(*Main.password_textbox).clear()
        self.driver.find_element(*Main.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Main.login_button).click()
        
       
       
        