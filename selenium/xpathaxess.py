import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

serv_obj = Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options,service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()


# #Self
# text = driver.find_element(By.XPATH,"//p[normalize-space()='Username : Admin']/self::p").text
# print(text)
#
# #Parant
#
# text = driver.find_element(By.XPATH,"//p[normalize-space()='Username : Admin']/parent::div").text
# print(text)
#
# #Child
#
# text = driver.find_element(By.XPATH,"//p[normalize-space()='Username : Admin']/ancestor::div/child::div").text
# print(len(text))
#
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()
# time.sleep(4)
#
# #Anistitor
#
# #text = driver.find_element(By.XPATH,"//div[contains(text(),'Russel.Hamilton')]/ancestor::div").text
# #print(len(text),(text))
#
#
# abc = driver.find_elements(By.XPATH,"//div[contains(text(),'Russel.Hamilton')]/ancestor::div/following::*")
# print("No of decendent nodes",len(abc))


