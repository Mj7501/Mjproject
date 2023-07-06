import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


opt_obj = webdriver.ChromeOptions()
opt_obj.add_experimental_option("detach",True)
serv_obj = Service(r"C:\Users\Lenovo\Desktop\chromedriver\chromedriver_win32 (1)/chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj,options=opt_obj)

driver.get("https://www.amazon.in/")


page_title = driver.title
print(page_title)


page_url = driver.current_url
print(page_url)


# page_source = driver.page_source
# print(page_source)


element =  driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")
if element.is_displayed():
    print("element is displayes")
else:
    print("Element is not available ")



dropdown = driver.find_element(By.XPATH,"//div[normalize-space()='EN']").click()

select = Select(dropdown)


driver.quit()











