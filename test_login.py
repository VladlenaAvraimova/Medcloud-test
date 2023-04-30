from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://dev7-analizi-mis.bizonoff-dev.net/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    input1 = browser.find_element(By.ID, "input-el-2")  
    input1.click()
    input1.send_keys("test@mail.fake")
    input2 = browser.find_element(By.ID, "input-el-3")
    input2.click()
    input2.send_keys("2Devel0New1Pass7")
    button = browser.find_element(By.ID, "button-el-4")
    button.click()
    work_space=browser.find_element(By.CSS_SELECTOR, "#crm-dashboard > h1")
    work_text=work_space.text
    assert(work_text == "Робочий стіл")
finally:
    # 
    time.sleep(5)
    # закриття браузера після всіх маніпуляцій
    browser.quit()

# в кінці залишаємо пусту строку