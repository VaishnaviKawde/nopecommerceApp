from selenium import webdriver
from pageObjects.loginPage import login
import pytest
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen


class Test_001_login:
    baseurl = Readconfig.getApplicationurl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()

    logger=LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regrassion
    def test_homePageTitle(self, setup):
        self.logger.info("**************** Test_001_login *********************")
        self.logger.info("**************** verifing home page title *********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        Act_title = self.driver.title
        if Act_title == "Your store. Login":
            assert True
            self.logger.info("****************** HOME PAGE TITLE TEST PASS *********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            assert False
            self.logger.info("**************** HOME PAGE TITLE TEST FAILED ***********************")
            self.driver.close()

    def test_login(self,setup):
        self.logger.info("*************** Home page Title Page  Pass ***************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.obj = login(self.driver)
        self.obj.setusername(self.username)
        self.obj.setpassword(self.password)
        self.obj.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*******************  LOGIN TEST PASS **************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.logger.info("**********************  LOGIN TEST PASS ***************************")
            self.driver.close()









