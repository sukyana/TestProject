import json
from tkinter import messagebox
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


def test_login_components():
    service = Service(executable_path="D:\\Web Driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.spotify.com/us/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F")
    passed = 0
    false = 0
    print("----------------------Report-----------------------")

    try:
        title = driver.title
        assert title == "Sign up for free to start listening."
    except Exception as e:
        print(e, "Check title false")
        false += 1
    else:
        print("Check title passed")
        passed += 1
    driver.implicitly_wait(0.5)

    try:
        url = driver.current_url
        assert url == "https://www.spotify.com/us/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F"
    except Exception as e:
        print(e, "Check url false")
        false += 1
    else:
        print("Check url pass")
        passed += 1
    driver.implicitly_wait(0.5)

    try:
        appname = driver.find_element(by=By.CLASS_NAME, value="app-name")
        appname_text = appname.text
        assert appname_text == "Sign up for free to start listening."
    except Exception as e:
        print(e, "Check app name false")
        false += 1
    else:
        print("Check app name passed")
        passed += 1
    driver.implicitly_wait(0.5)

    try:
        message = driver.find_element(by=By.CLASS_NAME, value="welcome")
        value = message.text
        assert value == "Welcome"
    except Exception as e:
        print(e, "Check sub header false")
        false += 1
    else:
        print("Check sub header passed")
        passed += 1
    driver.implicitly_wait(0.5)

    try:
        login_button_colour = Color.from_string(driver.find_element(By.CLASS_NAME, 'btn-primary')
                                                .value_of_css_property("background-color"))
        assert login_button_colour.hex == '#3c8dbc'
    except Exception as e:
        print(e, "Check button colour false")
        false += 1
    else:
        print("Check button colour passed")
        passed += 1
    driver.implicitly_wait(0.5)

    try:
        driver.find_element(By.NAME, "username").is_displayed()
    except Exception as e:
        print(e, "Check username display false")
        false += 1
    else:
        print("Check username display passed")
        passed += 1
    driver.implicitly_wait(0.5)

    # try:
    #     up = json.loads('{"username":"admin","password":"20081"}')
    #     driver.find_element(By.NAME, "username").send_keys(up["username"])
    #     driver.find_element(By.NAME, "password").send_keys(up["password"] + Keys.ENTER)
    # except Exception as e:
    #     print(e, "Check login with invalid username and password false")
    #     false += 1
    # else:
    #     print("Check login with invalid user and password passed")
    #     passed += 1
    # driver.implicitly_wait(0.5)

    try:
        up1 = json.loads('{"username":"admin.test","password":"2008"}')
        driver.find_element(By.NAME, "username").send_keys(up1["username"])
        driver.find_element(By.NAME, "password").send_keys(up1["password"] + Keys.ENTER)
    except Exception as e:
        print(e, "Check login with valid username and password false")
        false += 1
    else:
        print("Check login with valid user and password passed")
        passed += 1
    driver.implicitly_wait(0.5)
    driver.stop_client()
    report = "Total TC: Passed= {},  False= {}"
    report_alert = "Passed= {},  False= {}"
    print(report.format(passed, false))
    print("----------------------END-----------------------")
    messagebox.showinfo("Total TC", report_alert.format(passed, false))

test_login_components()
