# 1. https://nichethyself.com/tourism/home.html
# 2. Go to "Customized tours"
# 3. Select "Home Stay" in preferred stay dropwdown/combo.
# 4. Click on England checkbox
# 5. From above now click on "Contact Us" menu on top right corner
# 6. On "Contact Us" window, click on Search icon.
# 7. Enter "London" on the pop window and click on OK.
# 8. Close "Contact Us" window and click on "Submit" button on customized tour
import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
opt_obj = webdriver.ChromeOptions()
opt_obj.add_experimental_option("detach",True)
serv_obj = Service(r"C:\Users\Lenovo\Desktop\New folder\chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=opt_obj)
driver.get("https://nichethyself.com/tourism/home.html")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.XPATH,"/html/body/div[1]/a[1]").click()
window  = driver.window_handles
child_window = window[1]
driver.switch_to.window(child_window)


drop_down = Select(driver.find_element(By.XPATH,"//*[@id='days']"))
drop_down.select_by_visible_text("Home Stay")

driver.find_element(By.XPATH,"//*[@id='international']/form/div[2]/label/input").click()
driver.find_element(By.NAME,"members").send_keys("10 members")
driver.find_element(By.NAME,"days").send_keys("15 days")
driver.find_element(By.NAME,"countries").send_keys("India")

driver.find_element(By.XPATH,"//*[@id='myNavbar']/ul/li[6]/a").click()

way = Select(driver.find_element(By.NAME,"way"))
way.select_by_index(1)
driver.find_element(By.XPATH,"//*[@id='dropdowny']/input[1]").click()

act = ActionChains(driver)
act.key_down(Keys.SHIFT)
driver.find_element(By.XPATH,"//*[@id='sel']/option[6]").click()
driver.find_element(By.XPATH,"//*[@id='sel']/option[7]").click()
act.key_up(Keys.SHIFT)

driver.find_element(By.XPATH,"//*[@id='dropdowny']/input[2]").click()
time.sleep(2)

driver.back()
driver.back()


# driver.get("https://nichethyself.com/tourism/home.html")
driver.find_element(By.XPATH,"//a[normalize-space()='My Account']").click()
time.sleep(2)
driver.close()













