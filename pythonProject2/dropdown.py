import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



opt_obj = webdriver.ChromeOptions()
opt_obj.add_experimental_option("detach",True)
serv_obj = Service(r"C:\Users\Lenovo\Desktop\chromedriver\chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=opt_obj)

driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

element = driver.find_element(By.XPATH,"//select[@id='first']")
drp = Select(element)
drp.select_by_index(2)
time.sleep(2)
drp.select_by_value("Google")
drp.