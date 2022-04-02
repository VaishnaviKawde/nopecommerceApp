import time
from selenium import webdriver
from pageObjects.loginPage import login
import pytest
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
from utilities.XLUtils import XLUtils
import logging
import openpyxl

class Test_002_DDT_login:
    baseurl = Readconfig.getApplicationurl()
    path="./testData/testdata.xlsx"
    logger=LogGen.loggen()

    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        # self.driver.maximize_window()
        lst_status = []
        self.obj = login(self.driver)
        # self.rows=XLUtils.getrowCount(self.path,"Sheet1")


        for r in range(2,6):
            self.user = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password =XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)
            self.obj.setusername(self.user)
            self.obj.setpassword(self.password)
            self.obj.clicklogin()
            # time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    print("***** Passed")
                    self.obj.clicklogout()
                    # lst_status.append("pass")
                elif self.exp == "fail":
                    print("***** Faild")
                    # lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    print("***** faild")
                    self.obj.clicklogout()
                    # lst_status.append("fail")
                elif self.exp == "fail":
                    print("***** Passed")
                    # lst_status.append("pass")
        self.driver.close()







