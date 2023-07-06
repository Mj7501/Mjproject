from pageObjects.HomePage import HomePage
from pageObjects.ReegisterPage import AccountRegistrationPage
from utilities import randonstring
import os
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Accountreg:
    baseUrl = ReadConfig.ApplicationUrl()
    logger = LogGen.loggen()

    def test_account_reg(self,setup):
        self.logger.info("*** test execution started ***")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.Clicksignup()
        self.hp.clicknamae("Manoj")
        self.email=randonstring.random_string_generator()+'@xyz.com'
        self.hp.Clickemail(self.email)
        #self.hp.Clickemail("fvgbh@cfcvgb.cfvgbh")
        self.hp.clicksignupbtn()

        self.reg = AccountRegistrationPage(self.driver)
        self.reg.ClickMrMrs()
        self.reg.SetPwd("fghjk")
        self.reg.SetFirstName("Manojjj")
        self.reg.SetLastName("joshi")
        self.reg.SetCompanyName("xnxx")
        self.reg.SetAddress1("Pune")
        self.reg.SetAddress2("Punee")
        self.reg.SetStateName("vbn")
        self.reg.SetCityName("vbngh")
        self.reg.SetZipCode("52332")
        self.reg.SetMobileno("dfghj52")
        self.reg.ClickCreateaccount()
        self.confmsg=self.reg.Getconformationmsg()

        if self.confmsg=='Congratulations! Your new account has been success':
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"tst_account_reg_s.png")
            self.driver.close()
            assert False
        self.logger.info("*** test execution ended ***")










