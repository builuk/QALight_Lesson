from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xpath_dumskaya as x
import user_data

driver = webdriver.Chrome()
driver.set_window_position(2000, 600)
driver.maximize_window()
url = 'https://dumskaya.net/'
driver.get(url)
#https://selenium-python.readthedocs.io/waits.html
#https://www.selenium.dev/documentation/webdriver/waits/

enter_button = driver.find_element(By.XPATH, x.enter_button)
enter_button.click()
time.sleep(3)

registration_button = driver.find_element(By.XPATH, x.registration_button)
registration_button.click()
time.sleep(5)

email_field = driver.find_element(By.XPATH, x.email_field)
email_field.send_keys(user_data.email)
time.sleep(3)

nick_field = driver.find_element(By.XPATH, x.nick_field)
nick_field.send_keys(user_data.nick)
time.sleep(3)

password_field = driver.find_element(By.XPATH, x.password_field)
password_field.send_keys(user_data.password)
time.sleep(3)

password2_field = driver.find_element(By.XPATH, x.password2_field)
password2_field.send_keys(user_data.password)
time.sleep(3)

male_radio = driver.find_element(By.XPATH, x.male_radio)
male_radio.click()
time.sleep(3)

finish_button = driver.find_element(By.XPATH, x.finish_button)
finish_button.click()

time.sleep(5)
time.sleep(300)