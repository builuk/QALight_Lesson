from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def base_button(d,xpath):
    elem = WebDriverWait(d, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elem.click()

def base_field(d,xpath,data):
    elem = WebDriverWait(d, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elem.send_keys(data)

def base_label(d,xpath):
    elem = WebDriverWait(d, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    return elem.text