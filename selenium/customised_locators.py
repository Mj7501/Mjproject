import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/login.php")
driver.maximize_window()
time.sleep(3)
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("9422153254")
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("9422153254")
time.sleep(3)
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("9545529175")
#driver.find_element(By.CSS_SELECTOR,"input[autocomplete=current-password]").send_keys("9545529175")
driver.find_element(By.CSS_SELECTOR,"[autocomplete=current-password]").send_keys("9545529175")
time.sleep(3)
driver.find_element(By.ID,"u_0_4_40").click()
time.sleep(3)