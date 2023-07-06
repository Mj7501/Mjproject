import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
opt_obj = webdriver.ChromeOptions()
opt_obj.add_experimental_option("detach",True)
serv_obj = Service(r"C:\Users\Lenovo\Desktop\New folder\chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=opt_obj)
driver.get("https://nichethyself.com/tourism/home.html")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='My Account']").click()
driver.find_element(By.XPATH,"//a[@title='Tooltip']").click()
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,"#signup > div > div"))

time.sleep(2)


time.sleep(3)
driver.close()