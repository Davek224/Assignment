import conftest
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "PythonAutomationFramework_1-master"))
from pages.HomePage.locators import *

class Main():
    profile_button = Page.welcome_link_id


class profileboard():
    logout =  Page.logout_link_xpath
