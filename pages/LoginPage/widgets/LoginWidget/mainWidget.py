import conftest
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "PythonAutomationFramework_1-master"))
from pages.LoginPage.locators import *

class Main():
    username_textbox = Page.username_id
    instance_textbox = Page.instance_id
    password_textbox = Page.password_id
    login_button     = Page.login_button_id



