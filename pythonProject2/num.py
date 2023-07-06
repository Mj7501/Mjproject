import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt_obj = webdriver.ChromeOptions()
opt_obj.add_experimental_option("detach",True)
serv_obj = Service(r"C:\Users\Lenovo\Desktop\chromedriver\New folder\chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=opt_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

reg = driver.find_element(By.XPATH,"//a[normalize-space()='Register']")
reg.click()
login = driver.find_element(By.XPATH,"//a[normalize-space()='Log in']")
#login.click()

driver.find_element(By.XPATH,"//input[@id='gender-female']").click()
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Manoj")
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys("Joshi")
driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']").send_keys("10")
driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']").send_keys("October")
driver.find_element(By.XPATH,"//select[@name='DateOfBirthYear']").send_keys("1995")
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("mj@gmail.com")
driver.find_element(By.XPATH,"//input[@id='Company']").send_keys("Mangalram")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("123654")
driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys("123654")
driver.find_element(By.XPATH,"//button[@id='register-button']").click()

abd=driver.find_element(By.XPATH,"//div[@class='result']").is_displayed()
print(abd)
time.sleep(5)
driver.close()



#//div[@class='result']












#time.sleep(3)







#driver.close()