from selenium import webdriver
import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "PythonAutomationFramework_1-master"))
from pages.LoginPage.flows import LoginPage
from pages.HomePage.flows import HomePage
from pages.EventsPage.flows import EventsPage
from utils import  utils as utils
import allure
import moment
import time

@pytest.mark.usefixtures("test_setup")
class TestLogin():
    
    def test_login(self):
        try:
        
            driver = self.driver
            driver.get(utils.URL)

            login = LoginPage(driver)
            homepage= HomePage(driver)
            eventspage = EventsPage(driver)

            login.enter_username(utils.USERNAME)
            login.enter_instance(utils.INSTANCE)
            login.enter_password(utils.PASSWORD)
            login.click_login()
            homepage.navigate_events_screen()
            eventspage.search_value("NewUser")
            time.sleep(5)
            eventspage.value_exists("NewUser")
            time.sleep(5)
            eventspage.search_value("Purchase")
            time.sleep(5)
            eventspage.value_exists("Purchase")
            time.sleep(5)
            
            
            
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                        attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/Users/Dror/Desktop/Automation/PythonAutomationFramework_1-master/screenshots/" + screenshotName + ".png")
            raise

        except:
            print("There was an exception")

            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                        attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "C:/Users/Dror/Desktop/Automation/PythonAutomationFramework_1-master/screenshots/" + screenshotName + ".png")
            raise

    # def test_login(self):
        
    #         driver = self.driver
    #         driver.get(utils.URL)

    #         login = LoginPage(driver)
    #         login.enter_username(utils.USERNAME)
    #         login.enter_instance(utils.INSTANCE)
    #         login.enter_password(utils.PASSWORD)
    #         login.click_login()
            
        

    # def test(self):
        
    #     try:
    #         driver = self.driver
    #         homepage = HomePage(driver)
    #         # homepage.welcome_link_is_displayed()
            
    #         homepage.navigate_events_screen()
    #         homepage.

    #     except AssertionError as error:
    #         print("Assertion error occurred")
    #         print(error)
    #         currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
    #         testName = utils.whoami()
    #         screenshotName = testName+"_"+currTime
    #         allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
    #                       attachment_type=allure.attachment_type.PNG)

    #         driver.get_screenshot_as_file("C:/Users/Dror/Desktop/Automation/PythonAutomationFramework_1-master/screenshots/" + screenshotName + ".png")
    #         raise

    #     except:
    #         print("There was an exception")

    #         currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
    #         testName = utils.whoami()
    #         screenshotName = testName + "_" + currTime
    #         allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
    #                       attachment_type=allure.attachment_type.PNG)
    #         driver.get_screenshot_as_file(
    #             "C:/Users/Dror/Desktop/Automation/PythonAutomationFramework_1-master/screenshots/" + screenshotName + ".png")
    #         raise
            


        # finally:
        #     print("I am inside finally block")


