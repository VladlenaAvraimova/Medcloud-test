from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import unittest

class TestResult(unittest.TestCase):
    def test_result_success(self):
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
         buttonorder = browser.find_element(By.CSS_SELECTOR, "#crm > div > div.admin-menu > ul > div.navbar-buttons > button")
         buttonorder.click()
         time.sleep(1)
         input_last_name = browser.find_element(By.ID, "search-autocomplete-input-12")  
         input_last_name.click()
         input_last_name.send_keys("Іваненко")
         input_first_name = browser.find_element(By.ID, "search-autocomplete-input-13")  
         input_first_name.click()
         input_first_name.send_keys("Степан")
         selectgender=browser.find_element(By.ID, "select-loaded-18").click()
         selectfem= browser.find_element(By.CSS_SELECTOR,"#crm-med-center-cart > div > div > div.col-lg-9.col-md-8.col-sm-12 > div.wrapper.patient-wrapper.page-background.mb-25 > div:nth-child(6) > div:nth-child(3) > div > div.hidden-menu > div > ul > li:nth-child(2)")
         selectfem.click()
         buttonanalyses = browser.find_element(By.CSS_SELECTOR, "#crm-med-center-cart > div > div > div.col-lg-9.col-md-8.col-sm-12 > div.wrapper.order-wrapper > ul > li:nth-child(4) > span")
         buttonanalyses.click()
         input_search = browser.find_element(By.ID, "input-el-105")  
         input_search.click()
         browser.execute_script("window.scrollBy (0,100);")
         input_search.send_keys("B150") 
         browser.execute_script("window.scrollBy (0,500);")
         time.sleep(1)
         buttonadd = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/span/button")
         buttonadd.click()
         browser.execute_script("window.scrollBy (0,500);")
         time.sleep(2)
         buttonconfirm = browser.find_element(By.CSS_SELECTOR, "#button-el-42")
         buttonconfirm.click()
         time.sleep(5)
         buttonthreedots = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[6]/div[1]/div[1]/div[10]/div[1]/div[1]/button")
         buttonthreedots.click()
         button_to_result = browser.find_element(By.CSS_SELECTOR, "#crm-med-center-orders > div > div.items > div:nth-child(1) > div:nth-child(1) > div.order-prew-item.float-right.buttons-mobile > div.order-prew-item.button-block > div.dropdown.show.open > div > div")
         button_to_result.click()
         time.sleep(2)
         input_result= browser.find_element(By.XPATH,  "/html/body/div/div[2]/div/div/div[5]/div/div[1]/div[5]/div/input")
         input_result.send_keys("1") 
         buttonsafe = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/div/div[1]/div[12]/div[1]/span/button")
         buttonsafe.click()
         time.sleep(3)
         button_approve = browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[5]/div/div[1]/div[12]/div[2]/span/button")
         #button_approve = WebDriverWait (browser,5).until(EC.element_to_be_clickable ((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/div/div[1]/div[12]/div[2]/span/button")))
         button_approve.click()
         time.sleep(2)
         success_label = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/p")
         success_text= success_label.text
         #print ("ERROR_TEST", success_text)
         self.assertEqual(success_text,"Результати затверджено","Результати затверджено")
  




         
    if (__name__ == "__main__"):
        unittest.main()

# в кінці залишаємо пусту строку