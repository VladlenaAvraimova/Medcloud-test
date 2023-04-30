from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import unittest

class TestRegistration(unittest.TestCase):
    def test_login_success(self):
         link = "https://dev7-analizi-mis.bizonoff-dev.net/"
         browser = webdriver.Chrome()
         browser.get(link)
         time.sleep(1)
         inputlog = browser.find_element(By.ID, "input-el-2")  
         inputlog.click()
         inputlog.send_keys("test@mail.fake")
         inputpass = browser.find_element(By.ID, "input-el-3")
         inputpass.click()
         inputpass.send_keys("2Devel0New1Pass7")
         buttonlog = browser.find_element(By.ID, "button-el-4")
         buttonlog.click()
         time.sleep(1)
         work_space=browser.find_element(By.CSS_SELECTOR, "#crm-dashboard > h1")
         work_text=work_space.text
         self.assertEqual(work_text,"Робочий стіл","Робочий стіл")
    def test_login_fail(self):
         link = "https://dev7-analizi-mis.bizonoff-dev.net/"
         browser = webdriver.Chrome()
         browser.get(link)
         time.sleep(1)
         inputlog = browser.find_element(By.ID, "input-el-2")  
         inputlog.click()
         inputlog.send_keys("test@mail.fake")
         inputpass = browser.find_element(By.ID, "input-el-3")
         inputpass.click()
         inputpass.send_keys("2Devel0New1Pass72")
         buttonlog = browser.find_element(By.ID, "button-el-4")
         buttonlog.click()
         time.sleep(1)
         log_label=browser.find_element(By.CSS_SELECTOR, "#crm-login > div > div.wrapper.page-background > div > h1")
         log_text= log_label.text
         self.assertEqual(log_text, "Вхід в систему", "Вхід в систему")
   
if (__name__ == "__main__"):
    unittest.main()

# в кінці залишаємо пусту строку