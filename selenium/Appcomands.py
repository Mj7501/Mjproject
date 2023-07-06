import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

serv_obj = Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options,service=serv_obj)

# driver.get("https://www.facebook.com/")
# driver.maximize_window()
#
# #print(driver.title)
#
# search_botton = driver.find_element(By.XPATH,"//input[@id='email']")
# print("Searchbox enabled - ",search_botton.is_enabled())
# print("Search box Avliable - ",search_botton.is_selected())
#
# driver.find_element(By.ID,"u_0_0_4q").click()

#
# driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# #
# rd_male = driver.find_element(By.XPATH,"//label[normalize-space()='Male']//input[@name='optradio']")
# rd_female = driver.find_element(By.XPATH,"//label[normalize-space()='Female']//input[@name='optradio']")
# rd_female.click()
# rd_male.click()
# print("Male_radio_botton",rd_male.is_selected())
# print("Female_radio_botton",rd_female.is_selected())


driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")
# driver.get("https://www.facebook.com/")
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()

# element = driver.find_element(By.XPATH,"//footer[@class='footer']//li")
# print(element.text)

# element = driver.find_elements(By.XPATH,"//a[normalize-space()='Demo Home']")
# print(len(element))
# print(element[0].text)

# element = driver.find_elements(By.XPATH,"//footer[@class='footer']//li")
# print(len(element))
# #print(element[0].text)
# for ele in element:
#      print(ele.text)
#element= driver.find_elements(By.TAG_NAME,"Nobel")
#print("log found - ",len(element))

driver.find_element(By.XPATH,"//li[@class='tree-branch']//a[@href='#'][normalize-space()='Input Forms']").click()
driver.find_element(By.XPATH,"//li[@class='tree-branch']//ul//li//a[normalize-space()='Simple Form Demo']").click()
driver.find_element(By.XPATH,"//input[@id='user-message']").send_keys("Manoj is great")

Textbox = driver.find_element(By.XPATH,"//input[@id='user-message']")
print("result of text",Textbox.text)
Textbox.clear()
print("result of get attribute - ",Textbox.get_attribute('value'))

txt = driver.find_element(By.XPATH,"//button[normalize-space()='Show Message']")
print("result of text---",txt.text)
print("result of attribute = ",txt.get_attribute('value'))
print("result of attribute = ",txt.get_attribute('type'))






























