import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login_Page
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

# give class name as testcase id
class Test_001_Login:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger  = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepage(self,setup):
        self.logger.info("----Test001 Login ----")
        self.logger.info("----verifying home page title----")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title == "nopCommerce demo store. Login":
            assert True
            self.logger.info("---home page title is passed-----")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            self.logger.info("---home page title is failed-----")
            assert False


    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("---verifying login test-----")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login_Page(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("---login page title is passed-----")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("---login page title is failed-----")
            assert False

