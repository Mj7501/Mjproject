from selenium import webdriver

#
# TEST Case 1
# 1) Open web browser
# 2) Open Url
# 3) Emter username (Admin)
# 4) Enter password (admin)
# 5) Click on login
# 6) Capture title of the home page
# 7) Verify title of  home page (OrengeHRM)
# 8) Close Browse
import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# #from  selenium .webdriver.common.by import By
# driver = webdriver.Chrome(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
# driver.get("https://www.facebook.com/")
# driver.find_element_by_name("email").send_keys("Admin")

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.instagram.com/")
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("455666662563")
time.sleep(2)
driver.find_element(By.NAME,"password").send_keys("4555885577")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id="loginForm"]/div/div[3]/button").cli








