from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.set_window_position(2000, 600)

driver.maximize_window()

url = "https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"

driver.get(url)

q1_element = driver.find_element(By.NAME, "q1")
q1_element.send_keys("n")

q2_element = driver.find_element(By.NAME, "q2")
q2_element.send_keys("10")

q3_element = driver.find_element(By.NAME, "q3")
q3_element.send_keys("8")

# q9_element = driver.find_element(By.NAME, "q9")
# q9_element.click()

q9_element = driver.find_element(By.XPATH, '//input[@name="q9" and @value="b"]')
#//input[@name="q9"][@value="b"]
q9_element.click()


q19_b_element = driver.find_element(By.XPATH, '//input[@name="q19" and @value="b"]')
#//input[@name="q9"][@value="b"]
q19_b_element.click()
time.sleep(2)
q19_d_element = driver.find_element(By.XPATH, '//input[@name="q19" and @value="d"]')
#//input[@name="q9"][@value="b"]
q19_d_element.click()
time.sleep(2)
q19_b_element.click()

time.sleep(300)