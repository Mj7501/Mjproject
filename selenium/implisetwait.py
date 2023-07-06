from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

serv_obj = Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=opt,service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")
driver.find_element(By.XPATH,"//li[@class='tree-branch']//a[@href='#'][normalize-space()='Input Forms']").click()
driver.find_element(By.XPATH,"//li[@class='tree-branch']//ul//li//a[normalize-space()='Simple Form Demo']").click()

