# coding = utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/huanghao/Desktop/chromedriver') 

driver.get("http://localhost:8080/#/login")
time.sleep(2)
driver.find_element_by_xpath("//input[@type='text']").send_keys("188833389")
driver.find_element_by_xpath("//input[@type='password']").send_keys("abcdefghijklmnopqrstuvwxyz0123456789")
time.sleep(1)
driver.find_element_by_class_name("btn").click()
print driver.title
time.sleep(200)
driver.quit()