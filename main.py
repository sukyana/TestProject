from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


def test_login_components():
    service = Service(executable_path="D:\Web Driver\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://10.120.100.96:8080/WingMCUAT/login.html")

    title = driver.title
    assert title == "Wing MC | Log in"
    if (driver.title==title):
        print("Check title passed")
    else:
        print("Check title failed")

    driver.implicitly_wait(0.5)

    login_button_colour = Color.from_string(driver.find_element(By.CLASS_NAME, 'btn-primary').value_of_css_property('background-color'))
    assert login_button_colour.hex == '#3c8dbc'


    is_email_visible = driver.find_element(By.NAME, "username").is_displayed()
    if (is_email_visible==bool(1)):
        print("Check email visible passed")
    else:
        print("Check email visible failed")
    message = driver.find_element(by=By.CLASS_NAME, value="welcome")
    value = message.text
    assert value == "Welcome"
    if (value == "Welcome3"):
        print("Check message passed")
    else:
        print("Check message failed")

    driver.implicitly_wait(0.5)

    driver.find_element(By.NAME, "username").send_keys("admin.test")
    driver.find_element(By.NAME, "password").send_keys("2008" + Keys.ENTER)

    driver.quit()
test_login_components()