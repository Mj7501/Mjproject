import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests as requests
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

serv_obj = Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver  = webdriver.Chrome(options=opt,service=serv_obj)

# driver.get("http://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
# driver.maximize_window()
#
# dropdown_ele = driver.find_element(By.XPATH,"//select[@id='select-demo']")
# dropday = Select(dropdown_ele)
# # Selct options from drop down
# dropday.select_by_value('Monday')
# abc = dropday.select_by_index(5)
# dropday.select_by_visible_text('Friday')
#
# all_opt = dropday.options
# print(len(all_opt))
#
# for opt in all_opt:
#     print(opt.text)
#

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
# time.sleep(2)
#
# alert_window = driver.switch_to.alert
#
# print(alert_window.text)
# alert_window.send_keys("78885222")
# #alert_window.accept()
# alert_window.dismiss()


driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")






























