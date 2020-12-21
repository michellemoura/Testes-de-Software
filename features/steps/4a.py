from behave import given, when, then
from selenium.webdriver.chrome.options import Options
import os
import sys
from features.steps.utils.main_functions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)


@given('that the user is logged in to the system3')
def step_impl(context):
    options = Options()
    options.add_argument('--incognito')
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'), options=options)
    context.driver.maximize_window()
    context.driver.get('https://teste.leadfortaleza.com.br/ead/login')

    username = context.driver.find_element_by_id('login')
    username.send_keys('alunoauditivo26')
    time.sleep(1)

    password = context.driver.find_element_by_id('password')
    password.send_keys('abcd1234')
    time.sleep(1)

    login_button = context.driver.find_element_by_id('login-btn')
    login_button.click()
    time.sleep(1)


@when('the user clicks on the open selections module')
def step_impl(context):
    login_button = context.driver.find_element_by_id('nav-item-5')
    login_button.click()


@then('the system shows open selections')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.ID, 'smallHeader')))
    meusCursos = context.driver.find_element_by_id('smallHeader').text
    assert meusCursos == "Inscrições Abertas (Fluxo Antigo)"
    time.sleep(2)
    context.driver.quit()



















'''
import time
from behave import *
from features.steps.utils.main_functions import Browser
from nose.tools import assert_equal
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def get_element(locator):
    # aguarda elemento estar visível na tela
    WebDriverWait(Browser.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
    # retorna elemento
    return Browser.driver.find_element(By.CSS_SELECTOR, locator)



@given('that is logged in the system3')
def step_impl(context):
    pass


@when('click on the open selections module')
def step_impl(context):
    button = get_element('[id="nav-item-5"]')
    button.click()
    time.sleep(3)


@then('the system shows open selections')
def step_impl(context):
    element = get_element('h2')
    assert_equal(element.text, 'Inscrições Abertas (Fluxo Antigo)')
    Browser.driver.quit()
'''