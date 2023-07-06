from selenium.webdriver.common.by import By


class HomePage():
    Link_myaccount_xpath ="//i[@class='fa fa-lock']"
    Link_regname_name ="name"
    Link_regemail_xpath ="//*[@id='form']/div/div/div[3]/div/form/input[3]"
    btn_signup_xpath ="//button[normalize-space()='Signup']"

    def __init__(self,driver):
        self.driver=driver


    def Clicksignup(self):
        self.driver.find_element(By.XPATH,self.Link_myaccount_xpath).click()

    def clicknamae(self,nme):
        self.driver.find_element(By.NAME,self.Link_regname_name).send_keys(nme)

    def Clickemail(self,email):
        self.driver.find_element(By.XPATH,self.Link_regemail_xpath).send_keys(email)

    def clicksignupbtn(self):
        self.driver.find_element(By.XPATH,self.btn_signup_xpath).click()

