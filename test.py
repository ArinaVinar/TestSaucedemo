import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

LOGIN = "standard_user"
PASSWORD = "secret_sauce"

def test():
    browser = webdriver.Chrome()

    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(LOGIN)
    browser.find_element(By.ID, "password").send_keys(PASSWORD)
    browser.find_element(By.ID, "login-button").click()
    time.sleep(5)
    products = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")

    assert products.text == "Products"

    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    remove = browser.find_element(By.ID, "remove-sauce-labs-backpack")

    assert remove.text == "Remove"

    browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()
    cart = browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div")

    assert cart.text == "Sauce Labs Backpack"

    browser.find_element(By.ID, "checkout").click()
    browser.find_element(By.ID, "first-name").send_keys("John")
    browser.find_element(By.ID, "last-name").send_keys("Orange")
    browser.find_element(By.ID, "postal-code").send_keys("456852")
    browser.find_element(By.ID, "continue").click()
    browser.find_element(By.ID, "finish").click()
    thank = browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/h2")

    assert thank.text == "Thank you for your order!"
    browser.quit()

test()
