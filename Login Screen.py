import json
from tkinter import messagebox

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


def test_login_components():
    service = Service(executable_path="D:\\Web Driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://accounts.spotify.com/en/login?continue=https")
    # frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'Button-y0gtbx-0 hpTULc sc-iCfMLu MPAeZ')))
    # status = webdriver.Chrome(service=service)
    # status.get("https://accounts.spotify.com/en/status")
    passed = 0
    false = 0
    print("----------------------Report-----------------------")

    try:
        title = driver.title
        assert title == "Login - Spotify"
    except Exception as e:
        print(e, "Check title false")
        false += 1
    else:
        print("Check title passed")
        passed += 1
    driver.implicitly_wait(0.5)

    try:
        url = driver.current_url
        assert url == "https://accounts.spotify.com/en/login?continue=https"
    except Exception as e:
        print(e, "Check url false")
        false += 1
    else:
        print("Check url pass")
        passed += 1
    driver.implicitly_wait(0.5)

    try:
        to_continue = driver.find_element(by=By.ID, value="login-to-continue")
        value = to_continue.text
        assert value == "To continue, log in to Spotify."
    except Exception as e:
        print(e, "Check to continue name false")
        false += 1
    else:
        print("Check to continue passed")
        passed += 1
    driver.implicitly_wait(0.5)

    iframe = driver.find_element(By.ID, "sign-up-link")
    ActionChains(driver)\
        .scroll_to_element(iframe)\
        .perform()

    try:
        email = driver.find_element(by=By.CLASS_NAME, value="Label-sc-1c0cv3r-0 jhxAUN")
        value1 = email.text
        assert value1 == "Email address or username"
    except Exception as e:
        print(e, "Check Email address or username false")
        false += 1
    else:
        print("Check Email address or username passed")
        passed += 1
    driver.implicitly_wait(0.5)

    # try:
    #     login_button_colour = Color.from_string(driver.find_element(By.CLASS_NAME, 'btn-primary')
    #                                             .value_of_css_property("background-color"))
    #     assert login_button_colour.hex == '#3c8dbc'
    # except Exception as e:
    #     print(e, "Check button colour false")
    #     false += 1
    # else:
    #     print("Check button colour passed")
    #     passed += 1
    # driver.implicitly_wait(0.5)

    try:
        driver.find_element(by=By.CLASS_NAME, value="Label-sc-1c0cv3r-0 jhxAUN").is_displayed()
    except Exception as e:
        print(e, "Check email display false")
        false += 1
    else:
        print("Check email display passed")
        passed += 1
    driver.implicitly_wait(0.5)

    try:
        up1 = json.loads('{"username":"admin.test","password":"2008"}')
        driver.find_element(By.NAME, "username").send_keys(up1["username"])
        driver.find_element(By.NAME, "password").send_keys(up1["password"] + Keys.ENTER)
    except Exception as e:
        print(e, "Check login with invalid username and password false")
        false += 1
    else:
        print("Check login with invalid user and password passed")
        passed += 1
    driver.implicitly_wait(0.5)

    try:
        up = json.loads('{"username":"yongseangyan@gmail.com","password":"Sukyankor"}')
        driver.find_element(By.ID, "login-username").send_keys(up["username"])
        driver.find_element(By.ID, "login-password").send_keys(up["password"] + Keys.ENTER)
    except Exception as e:
        print(e, "Check login with valid username and password false")
        false += 1
    else:
        print("Check login with valid user and password passed")
        passed += 1
    driver.implicitly_wait(0.5)
    driver.maximize_window()

    # try:
    #     choose = frame.find_element(By.CLASS_NAME, "Button-y0gtbx-0 hpTULc sc-iCfMLu MPAeZ")
    #     choose.click()
    # except Exception as e:
    #     print(e, "Check choose the Web Player false")
    # else:
    #     print("Check choose the Web Player passed")
    driver.stop_client()

    report = "Total TC {}: Passed= {},  False= {}"
    report_alert = "Passed= {},  False= {}"
    print(report.format(passed+false, passed, false))
    print("----------------------END-----------------------")
    messagebox.showinfo("Total TC", report_alert.format(passed, false))
# def test_seconde_screen_components():
#     status = webdriver.Chrome(service=service)
#     status.get("https://accounts.spotify.com/en/status")
test_login_components()
