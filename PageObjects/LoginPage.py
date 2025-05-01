from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# page object class
class Login_Page:
    # webelements
    txtbox_username_xpath = ("//input[@id='Email']")
    txtbox_pwd_xpath = ("xpath","//input[@id='Password']")
    btn_login_xpath = ("xpath","//button[normalize-space()='Log in']")
    link_logout_linktext=("link text","//a[normalize-space()='Logout']")

    # constructor - invoke at the time of object creation - come from actual test class to here
    def __init__(self,driver):
        self.driver = driver

#   #Action methods for every locator

    def set_username(self,username):
        # self.driver.find_element(self.)
        self.driver.find_element("xpath",self.txtbox_username_xpath).clear()
        self.driver.find_element("xpath",self.txtbox_username_xpath).send_keys(username)

    def set_password(self,password):
        # self.driver.find_element(self.txtbox_pwd_xpath).clear()
        # self.driver.find_element(self.txtbox_pwd_xpath).send_keys(password)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((self.txtbox_pwd_xpath))).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.btn_login_xpath))).click()

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.txtbox_pwd_xpath))).click()



