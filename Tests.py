from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By

service = Service(executable_path="D:\Web Driver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://10.120.100.96:8080/WingMCUAT/login.html")
username=driver.find_element(By.NAME, "username")
password=driver.find_element(By.NAME, "password")
ActionChains(driver) \
    .move_to_element(username) \
    .pause(1) \
    .click_and_hold() \
    .pause(1) \
    .send_keys("admin.test") \
    .move_to_element(password) \
    .pause(1) \
    .click_and_hold() \
    .pause(1)\
    .send_keys("2008") \
    .perform()
ActionBuilder(driver).clear_actions()