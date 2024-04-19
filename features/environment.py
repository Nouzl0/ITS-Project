#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import random
import string
import time

def before_all(context):
    
    # Get driver
    try:
        context.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=webdriver.ChromeOptions())
    except WebDriverException:
        context.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=webdriver.FirefoxOptions())
    context.driver.implicitly_wait(15)

    # Create random user data
    letters = string.ascii_lowercase
    context.first_name = context.name = ''.join(random.choice(letters) for i in range(10)) 
    context.last_name = context.name = ''.join(random.choice(letters) for i in range(10))
    context.email = context.name = ''.join(random.choice(letters) for i in range(10)) + "@gmail.com"
    context.password = context.name = ''.join(random.choice(letters) for i in range(10))

def after_all(context):
    context.driver.close()
    context.driver.quit()