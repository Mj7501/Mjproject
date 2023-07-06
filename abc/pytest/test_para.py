
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Testpara:
    @pytest.mark.parametrize('user,pwd',
                             [("Admin","admin123"),
                              ("Admin","adm112233"),
                              ("Adn","admin123"),
                              ("adm","qwe123")
                              ]
                             )
    def test_login(self,user,pwd):
        self.opt_obj=webdriver.ChromeOptions()
        self.opt_obj.add_experimental_option("detach",True)
        self.serv_obj = Service(r"C:\Users\Lenovo\Desktop\chromedriver\New folder\chromedriver_win32 (1)/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(7)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(user)
        self.driver.find_element(By.NAME,"password").send_keys(pwd)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        try:
            self.status = self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False