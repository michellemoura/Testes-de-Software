from behave import *
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


@given('that the user is logged in to the system')
def step_impl(context):
    options = Options()
    options.add_argument('--incognito')
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'), options=options)
    context.driver.maximize_window()
    context.driver.get('https://teste.leadfortaleza.com.br/ead/login')

    login(context)
    time.sleep(1)


@when('the user clicks the Enable high contrast option in the accessibility bar')
def step_impl(context):
    highContrast_button = context.driver.find_element_by_id('bt-highContrast')
    highContrast_button.click()
    time.sleep(3)
    highContrast_button.click()


@then('the system updates with high contrast colors')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.ID, 'bt-highContrast')))
    btncontrast = context.driver.find_element_by_id('bt-highContrast').get_attribute("aria-label")
    assert btncontrast == "Desabilitar alto contraste"
    time.sleep(2)
    context.driver.quit()