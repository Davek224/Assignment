from selenium.webdriver.common.by import By

class Page:
        welcome_link_id = By.ID, "welcome"
        logout_link_xpath = By.XPATH, "//a[contains(text(),'Logout')]"