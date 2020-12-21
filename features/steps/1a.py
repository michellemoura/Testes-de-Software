from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
from features.steps.utils.main_functions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)


@given('that the user is on the login page')
def step_impl(context):
    options = Options()
    options.add_argument('--incognito')
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'), options=options)
    context.driver.maximize_window()
    context.driver.get('https://teste.leadfortaleza.com.br/ead/login')


@when('the user provides a login with valid data')
def step_impl(context):
    username = context.driver.find_element_by_id('login')
    username.send_keys('alunoauditivo26')
    time.sleep(1)

    password = context.driver.find_element_by_id('password')
    password.send_keys('abcd1234')
    time.sleep(1)

    login_button = context.driver.find_element_by_id('login-btn')
    login_button.click()
    time.sleep(1)


@then('the system directs the user to the home page')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.ID, 'nav-item-0')))
    inicio = context.driver.find_element_by_id('nav-item-0').text
    assert inicio == "Início"
    time.sleep(2)
    context.driver.quit()


