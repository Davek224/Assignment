from selenium.webdriver.common.by import By

class Page:
        event_button = By.XPATH, "//a[@class='context-action']//span[contains(text(),'Events')]"
        analytics_button = By.XPATH, "//body[@class='layout-semi-dark shell']/div[@id='main']/div[@class='wrapper']/aside[@id='left-sidebar-nav']/ul[@id='menu-list']/div[@class='sidemenu-top']/li[@class='no-padding scrolled-menu-container']/ul[@class='collapsible scrollable-menu']/li[5]/a[1]"