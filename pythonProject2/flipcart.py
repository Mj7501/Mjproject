from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

opt_obj = webdriver.ChromeOptions()
opt_obj.add_experimental_option("detach",True)

serv_obj = Service(r"C:\Users\Lenovo\Desktop\chromedriver\chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=opt_obj)


driver.get("https://www.flipkart.com/")
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()

fashion =driver.find_element(By.XPATH,"//img[@alt='Mobiles']").click()
# mentop = driver.find_element(By.XPATH,"/")
# shirts =  driver.find_element(By.XPATH,"//div[@class='_3XS_gI']//a[3]")
#
# act = ActionChains(driver)
# act.move_to_element(fashion).move_to_element(mentop).move_to_element(shirts).click().perform()