



from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_Login():
    baseUrl = ReadConfig.ApplicationUrl()
    logger = LogGen.loggen()

    user= ReadConfig.getLoginEmail()
    pwd = ReadConfig.getUserPwd()



    def Test_login(self,setup):
        self.logger.info("Test 002 is started")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.Clicksignup()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setpassw(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.succesfulLoginAsmyAccount()
        if self.targetpage==True:
            assert True
        else:
            assert False

        self.driver.closed()









