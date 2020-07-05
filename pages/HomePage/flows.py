import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "PythonAutomationFramework_1-master"))
from pages.HomePage import locators
import selenium
from selenium.webdriver.common.by import By
from pages.HomePage.widgets.ProfileWidget.mainWidget import *
import time

class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def welcome_link_is_displayed(self):
        try:
            Element = self.driver.find_element(*Main.profile_button).isDisplayed()
            print(element)
            if Element == True:
                pass
        except Exception as e:
            print(e)


    def navigate_events_screen(self):
        self.driver.find_element(*Main.analytics_button).click()
        self.driver.find_element(*Main.events_button).click()
        time.sleep(5)

    def click_welcome(self):
        self.driver.find_element(*Main.profile_button).click()

    def click_logout(self):
        self.driver.find_element(*profileboard.logout).click()
       
        