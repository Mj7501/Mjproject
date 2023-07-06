from selenium.webdriver.common.by import By


class LoginPage:
    txt_emaiil_xpath ="input[data-qa='login-email']"
    txt_password_name = "password"
    btn_login_xpath = "//*[@id='form']/div/div/div[1]/div/form/button"
    logged_as_xpath = "//b[normalize-space()='Manoj Nithrudkar']"


    def __init__(self,driver):
        self.driver=driver


    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_emaiil_xpath).send_keys(email)
    def setpassw(self,password):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(password)
    def clickLogin(self,login):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
    def succesfulLoginAsmyAccount(self):
        try:
            return self.driver.find_element(By.XPATH,self.logged_as_xpath).is_desplayed()
        except:
            return False



