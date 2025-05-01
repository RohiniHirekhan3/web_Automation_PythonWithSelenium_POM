import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login_Page
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

# give class name as testcase id
class Test_002_DDT_Login:
    base_url = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"


    logger  = LogGen.loggen()

    def test_login(self,setup):
        self.logger.info("---verifying login test-----")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login_Page(self.driver)
        list =[]
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("number of rows",self.rows)
        for r in range(2,self.rows+1):
            self.user = XLUtils.ReadData(self.path,'Sheet1',r,1)
            self.password=XLUtils.ReadData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.ReadData(self.path,'Sheet1',r,3)

            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(15)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp == 'pass':
                    self.logger.info("***passed***")
                    self.lp.click_logout()
                    list.append("pass")
                elif self.exp=='fail':
                    self.logger.info("***fail***")
                    self.lp.click_logout()
                    list.append('fail')
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("***fail***")
                    list.append("fail")
                elif self.exp == 'fail':
                    self.logger.info("***pass***")
                    list.append("pass")

            if "fail" not in list:
                self.logger.info("***Login DDt test Passed***")
                assert True
            else:
                self.logger.info("***Login DDt test failed***")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login_ddt.png")
                assert False







