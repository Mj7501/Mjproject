from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests as requests
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

serv_obj = Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver  = webdriver.Chrome(options=opt,service=serv_obj)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
# driver.get("http://demo.seleniumeasy.com/table-data-download-demo.html")
# tabledata = driver.find_element(By.XPATH,"//table[@id='example']/tbody/tr[1]").text
# print(tabledata)

driver.switch_to.frame(0)
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("10/10/1995")

day = '10'
month = 'October'
year = '2020'

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yer = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if yer==year and mon==month:
     break;
    else:
        driver.find_element(By.XPATH,"//a[@title='Prev']").click()

dates =  driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tr/td/a")

for ele in dates:
    if ele.text == day:
        ele.click()
        break

dte = driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']//tr/td/a").text

print("The selected sate is =",dte)




