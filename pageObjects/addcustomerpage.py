import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Registration:
        Customers_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
        sub_Customers_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
        Add_button_Xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
        testbox_Email_id= "Email"
        testbox_password_id = "Password"
        testbox_Firstname_id = "FirstName"
        testbox_Lastname_id = "LastName"
        rediobutton_gender_male_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[5]/div[2]/div/div[1]/label"
        rediobutton_gender_female_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[5]/div[2]/div/div[2]/label"
        checkbox_exempt_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[8]/div[2]"
        checkbox_active_id = "Active"
        testbox_admin_comment_id = "AdminComment"
        rdMaleGender_id = "Gender_Male"
        rdfemaleGender_id = "Gender_Female"
        dateofbirth_id = "DateOfBirth"
        testbox_companyname_Xpath = "//*[@id='Company']"
        select_Newslatter_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/div"
        lititem_newslatterr_storename_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/div/ul/li/span[1]"
        lisitem_newslatter_teststore2_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/div/ul/li[2]/span[1]"
        select_customerroles_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div"
        select_custrole_Administrator_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div/ul/li[1]/span[1]"
        select_custrole_forummod_Xpath ="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div/ul/li[1]/span[1]"
        select_custrole_Guests_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div/ul/li[3]/span[1]"
        select_custrole_Register_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div/ul/li[4]/span[1]"
        select_custrole_vendors_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div/ul/li[5]/span[1]"
        select_manager_vendor_id = "VendorId"
        button_save_Xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

        def __init__(self, driver):
                self.driver = driver

        def clickoncustomermenu(self):
                self.driver.find_element(By.XPATH,self.Customers_Xpath).click()

        def clickoncustomermenuitem(self):
                self.driver.find_element(By.XPATH,self.sub_Customers_Xpath).click()

        def clickonAddNew(self):
                self.driver.find_element(By.XPATH,self.Add_button_Xpath).click()

        def setEmail(self,Email):
                self.driver.find_element(By.ID,self.testbox_Email_id).clear()
                self.driver.find_element(By.ID,self.testbox_Email_id).send_keys(Email)

        def setPassword(self,Password):
                self.driver.find_element(By.ID,self.testbox_password_id).clear()
                self.driver.find_element(By.ID,self.testbox_password_id).send_keys(Password)


        def setFirstName(self,FirstName):
                self.driver.find_element(By.ID, self.testbox_Firstname_id).clear()
                self.driver.find_element(By.ID,self.testbox_Firstname_id).send_keys(FirstName)


        def setLastName(self,LastName):
                self.driver.find_element(By.ID,self.testbox_Lastname_id).clear()
                self.driver.find_element(By.ID,self.testbox_Lastname_id).send_keys(LastName)

        def selectgender(self,gender):
                if gender == "Male":
                        self.driver.find_element(By.ID,self.rdMaleGender_id).click()
                elif gender == "Female":
                        self.driver.find_element(By.ID, self.rdfemaleGender_id).click()
                else:
                        self.driver.find_element(By.ID, self.rdMaleGender_id).click()

        def setdobirth(self,dob):
                self.driver.find_element(By.ID,self.dateofbirth_id).send_keys(dob)

        def setcompanyname(self,companyName):
                self.driver.find_element(By.XPATH,self.testbox_companyname_Xpath).send_keys(companyName)

        def taxattempt(self):
                self.driver.find_element(By.XPATH,self.checkbox_exempt_xpath).click()

        def selectnewslatter(self,news):
                self.driver.find_element(By.XPATH,self.select_Newslatter_Xpath).click()
                if news == "Your store name":
                        self.driver.find_element(By.XPATH,self.lititem_newslatterr_storename_Xpath).click()
                elif news == "Test store 2":
                        self.driver.find_element(By.XPATH,self.lisitem_newslatter_teststore2_xpath).click()
                else:
                        self.driver.find_element(By.XPATH, self.lititem_newslatterr_storename_Xpath).click()

        def maagerrole(self,value):
            self.driver.find_element(By.XPATH,self.select_customerroles_Xpath).click()
            if value == "Administrators":
                    self.listitem=self.driver.find_element(By.XPATH,self.select_custrole_Administrator_Xpath).click()
            elif value == "Forum Moderators":
                    self.listitem=self.driver.find_element(By.XPATH,self.select_custrole_forummod_Xpath).click()
            elif value == "Guests":
                    self.listitem=self.driver.find_element(By.XPATH,self.select_custrole_Guests_Xpath).click()
            elif value == "Register":
                    self.listitem=self.driver.find_element(By.XPATH, self.select_custrole_Register_Xpath).click()
            elif value == "vendors":
                    self.listitem=self.driver.find_element(By.XPATH, self.select_custrole_vendors_Xpath).click()
            else:
                    self.listitem = self.driver.find_element(By.XPATH, self.select_custrole_vendors_Xpath).click()

            time.sleep(5)
            self.driver.execute_script('argument[0].click();',self.listitem)


        def managervendor(self,vendor):
                ele = Select(self.driver.find_element(By.ID,self.select_manager_vendor_id))
                ele.select_by_visible_text(vendor)

        def selectactive(self):
                self.driver.find_element(By.ID,self.checkbox_active_id).click()

        def admin_Comment(self,comment):
                self.driver.find_element(By.ID,self.testbox_admin_comment_id).send_keys(comment)

        def savedata(self):
                self.driver.find_element(By.XPATH,self.button_save_Xpath).click()