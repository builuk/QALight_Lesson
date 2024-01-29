from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.set_window_position(2000, 600)

driver.maximize_window()

url = "https://test.mensa.no/"

driver.get(url)

xpath_template = '//div[contains(@id,"question_") and @style=""]'

def global_wait(xpath_template):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))

age1850_xpath = '//button[contains(@class,"ageselect_1850")]'
age1850_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, age1850_xpath)))
age1850_button.click()

start_id = 'startTest'
start_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, start_id)))
start_button.click()

global_wait(xpath_template)
q1_a_xpath = '//div[@id="question_0"]//div[@data-answerid="0"]'
q1_a_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q1_a_xpath)))
q1_a_button.click()

global_wait(xpath_template)
q2_b_xpath = '//div[@id="question_1"]//div[@data-answerid="1"]'
q2_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q2_b_xpath)))
q2_b_button.click()

global_wait(xpath_template)
q3_a_xpath = '//div[@id="question_2"]//div[@data-answerid="0"]'
q3_a_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q3_a_xpath)))
q3_a_button.click()

global_wait(xpath_template)
q4_b_xpath = '//div[@id="question_3"]//div[@data-answerid="1"]'
q4_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q4_b_xpath)))
q4_b_button.click()

global_wait(xpath_template)
q5_b_xpath = '//div[@id="question_4"]//div[@data-answerid="1"]'
q5_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q5_b_xpath)))
q5_b_button.click()

global_wait(xpath_template)
q6_a_xpath = '//div[@id="question_5"]//div[@data-answerid="0"]'
q6_a_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q6_a_xpath)))
q6_a_button.click()

global_wait(xpath_template)
q7_b_xpath = '//div[@id="question_6"]//div[@data-answerid="1"]'
q7_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q7_b_xpath)))
q7_b_button.click()

global_wait(xpath_template)
q8_a_xpath = '//div[@id="question_8"]//div[@data-answerid="0"]'
q8_a_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q8_a_xpath)))
q8_a_button.click()