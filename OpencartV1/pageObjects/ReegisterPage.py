from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    chk_mrormrs_id="uniform-id_gender1"
    txt_pwd_name="password"
    txt_firstname_id="first_name"
    txt_lastname_name="last_name"
    txt_company_name="company"
    txt_address1_name="address1"
    txt_address2_name="address2"
    txt_state_name="state"
    txt_city_name="city"
    txt_zip_id="zipcode"
    txt_mobile_id="mobile_number"
    btn_createaccount_xpath="//*[@id='form']/div/div/div/div/form/button"
    mst_accountcreated_xpath="//p[contains(text(),'Congratulations! Your new account has been success')]"

    def __init__(self,driver):
        self.driver = driver

    def ClickMrMrs(self):
        self.driver.find_element(By.ID,self.chk_mrormrs_id).click()

    def SetPwd(self,pwd):
        self.driver.find_element(By.NAME,self.txt_pwd_name).send_keys(pwd)

    def SetFirstName(self,fname):
        self.driver.find_element(By.ID,self.txt_firstname_id).send_keys(fname)

    def SetLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def SetCompanyName(self,comp):
        self.driver.find_element(By.NAME,self.txt_company_name).send_keys(comp)

    def SetAddress1(self,add1):
        self.driver.find_element(By.NAME,self.txt_address1_name).send_keys(add1)

    def SetAddress2(self,add2):
        self.driver.find_element(By.NAME, self.txt_address2_name).send_keys(add2)

    def SetStateName(self,staten):
        self.driver.find_element(By.NAME, self.txt_state_name).send_keys(staten)

    def SetCityName(self,cityn):
        self.driver.find_element(By.NAME, self.txt_city_name).send_keys(cityn)

    def SetZipCode(self,zip):
        self.driver.find_element(By.ID, self.txt_zip_id).send_keys(zip)

    def SetMobileno(self,mono):
        self.driver.find_element(By.ID, self.txt_mobile_id).send_keys(mono)

    def ClickCreateaccount(self):
        self.driver.find_element(By.XPATH,self.btn_createaccount_xpath).click()

    def Getconformationmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.mst_accountcreated_xpath).text
        except:
             pass