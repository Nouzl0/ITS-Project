#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException

from time import sleep

def start_driver():
    '''Get Firefox driver from Selenium Hub'''
    driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.FirefoxOptions())
    driver.implicitly_wait(15)

    # (jedno nebo druhe, zalezi na nastaveni prostedi)
    driver.get("http://opencart:8080/")

    return driver

def stop_driver(driver):
    driver.close()
    driver.quit()


# main function
if __name__ == "__main__":
    driver = start_driver()
    print("Driver started")
    sleep(10)
    stop_driver()
    print("Driver stopped")
    exit(0)