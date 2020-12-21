import time
from random import randint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(driver):
    username = driver.find_element_by_id('[name="login"]')
    username.send_keys('alunoauditivo26')

    password = driver.find_element_by_id('[name="password"]')
    password.send_keys('abcd1234')

    login_button = driver.find_element_by_id('[id="login-btn"]')
    login_button.click()