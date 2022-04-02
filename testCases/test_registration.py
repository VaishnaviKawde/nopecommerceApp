import random
import string
import pytest


from utilities.readproperties import Readconfig
from pageObjects.loginPage import login
from pageObjects.addcustomerpage import Registration
from utilities.readproperties import Readconfig


class Test_003_AddCustomer:
    baseURL = Readconfig.getApplicationurl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()


    def test_addcustomer(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.obj = login(self.driver)

        self.obj.setusername(self.username)
        self.obj.setpassword(self.password)
        self.obj.clicklogin()

        self.ob = Registration(self.driver)
        self.ob.clickoncustomermenu()
        self.ob.clickoncustomermenuitem()
        self.ob.clickonAddNew()

        self.email = random_generator()+"@gmail.com"
        self.ob.setEmail(self.email)
        self.ob.setPassword("123456")
        self.ob.setFirstName("ABC")
        self.ob.setLastName("XYZ")
        self.ob.selectgender("Male")
        self.ob.setdobirth("10/31/1996")
        self.ob.setcompanyname("Amdocs")
        self.ob.taxattempt()
        # self.ob.selectnewslatter("Your store name")
        self.ob.selectactive()
        self.ob.admin_Comment("Random comment")
        self.ob.savedata()

        self.obj.clicklogout()
        self.driver.close()



# this code generate randome 8 char for email address
def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))