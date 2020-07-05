import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "PythonAutomationFramework_1-master"))
from pages.HomePage import locators
import selenium
from selenium.webdriver.common.by import By
from pages.EventsPage.widgets.searchWidget import *
import time
from selenium.webdriver.common.keys import Keys

class EventsPage():

    def __init__(self, driver):
        self.driver = driver

    def search_value(self,value = None):
        self.driver.find_element(*Main.search_button).clear()
        self.driver.find_element(*Main.search_button).send_keys(value)
        self.driver.find_element(*Main.search_button).send_keys(Keys.RETURN)
        
    def value_exists(self, value):
        try:
            for element in self.driver.find_elements_by_class_name('events-row'):
                    elementName = element.text
                    assert value in elementName, "no string match"
                        
        except Exception as e:
            
            print(e + elementName)
            raise
        

    # def welc
    # ome_link_is_displayed(self):
    #     try:
    #         Element = self.driver.find_element(*Main.profile_button).isDisplayed()
    #         print(element)
    #         if Element == True:
    #             pass
    #     except Exception as e:
    #         print(e)

       
        