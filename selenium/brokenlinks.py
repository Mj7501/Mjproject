from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests as requests
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

serv_obj = Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver  = webdriver.Chrome(options=opt,service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME,'a')
count = 0

for link in all_links:
    url=link.get_attribute('href')
    resp = requests.head(url)
    if resp.status_code >= 400:
        print(url,"is Broken link")
        count+=1
    else:
        print(url, "is valid link")
print("Total links =",count)