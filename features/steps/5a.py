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


@given('that the user is logged in to the system4')
def step_impl(context):
    options = Options()
    options.add_argument('--incognito')
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'), options=options)
    context.driver.maximize_window()
    context.driver.get('https://teste.leadfortaleza.com.br/ead/login')

    login(context)
    time.sleep(1)


@when('the user clicks on the option user information and click on edit profile')
def step_impl(context):
    infouser_button = context.driver.find_element_by_id('avatar')
    infouser_button.click()
    time.sleep(2)

    profile_button = context.driver.find_element_by_class_name('text-secondary')
    profile_button.click()
    time.sleep(2)


@step('and the user clicks on the change photo button')
def step_impl(context):
    path = os.path.join(ROOT_DIR, 'src', 'natalead.jpg')
    context.driver.find_element_by_id('inputAvatar').send_keys(path)
    time.sleep(3)


@then('the system returns the changed photo')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'toast-message')))
    alteredphoto = context.driver.find_element_by_class_name('toast-message').get_attribute("aria-label")
    assert alteredphoto == "Foto alterada com sucesso!"
    time.sleep(2)
    context.driver.quit()