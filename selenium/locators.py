import time

import  selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(2)

#BY using id
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
time.sleep(2)
#driver.find_element(By.LINK_TEXT,"Register").click()
time.sleep(2)
#driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()
#time.sleep(1)
link: WebElement =driver.find_elements(By.TAG_NAME,"a")
time.sleep(2)
print(len(link))






