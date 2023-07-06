from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains,Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt =  webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)

serv_obj = Service(r"C:\Users\Lenovo\Desktop\STUDY\python\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=opt,service=serv_obj)

driver.get("https://text-compare.com/")

input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("Welcome to selenium")

act = ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL)
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

driver.find_element(By.XPATH,"//*[@id='compareButton']").click()

result = driver.find_element(By.XPATH,"//span[@class='messageForUser']")






