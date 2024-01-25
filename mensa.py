from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.set_window_position(2000, 600)

driver.maximize_window()

url = "https://test.mensa.no/"

driver.get(url)
age_1850 = driver.find_element(By.CLASS_NAME, 'ageselect_1850')
age_1850.click()
#Not so good //button[@class="age button btn btn-success ageselect_1850"]
#Better //button[contains(@class,"ageselect_1850")]
time.sleep(3)
start_button = driver.find_element(By.ID, 'startTest')
start_button.click()
time.sleep(3)
q1_a_button = driver.find_element(By.XPATH, '//div[@id="question_0"]/div/div/div[@data-answerid="0"]')
q1_a_button.click()
time.sleep(3)
#//div[@id="question_0"]//div[@data-answerid="0"]
q2_b_button = driver.find_element(By.XPATH, '//div[@id="question_1"]/div/div/div[@data-answerid="1"]')
q2_b_button.click()
time.sleep(3)
q3_c_button = driver.find_element(By.XPATH, '//div[@id="question_2"]/div/div/div[@data-answerid="2"]')
q3_c_button.click()
time.sleep(3)

time.sleep(30)