from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt_obj = webdriver.ChromeOptions()
opt_obj.add_experimental_option("detach",True)

serv_obj = Service(r"C:\Users\Lenovo\Desktop\chromedriver\chromedriver_win32 (1)/chromedriver.exe")

drivar = webdriver.Chrome(service=serv_obj,options=opt_obj)

drivar.get("https://www.amazon.in/")

drivar.find_element(By.XPATH,"//span[normalize-space()='Account & Lists']").click()
drivar.find_element(By.XPATH,"//input[@id='ap_email']").send_keys("8888212591")
drivar.find_element(By.XPATH,"//input[@id='continue']").click()
drivar.find_element(By.NAME,"password").send_keys("4455661122")
drivar.find_element(By.ID,"signInSubmit").submit()
drivar.quit()
print("tast 001 passed")