from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt =  webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

serv_obj = Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=opt,service=serv_obj)

driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//li[@class='tree-branch']//a[@href='#'][normalize-space()='Input Forms']").click()
driver.find_element(By.XPATH,"//li[@class='tree-branch']//ul//li//a[normalize-space()='Checkbox Demo']").click()

# 1 checkbox
#driver.find_element(By.XPATH,"//label[normalize-space()='Option 1']//input[@type='checkbox']").click()

driver.find_element(By.LINK_TEXT,"Demo Home").click()

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for link in links:
    print(link.text)













