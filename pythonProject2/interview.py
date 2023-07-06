import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt_obj = webdriver.ChromeOptions()
opt_obj.add_experimental_option("detach", True)
serv_obj = Service(r"C:\Users\Lenovo\Desktop\chromedriver\chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(options=opt_obj, service=serv_obj)

driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@id='nav-xshop']//a[contains(@class,'')][normalize-space()='Customer Service']").click()
