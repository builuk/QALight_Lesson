from selenium import webdriver
from pages import base
import helper.user.data as user_data
import time
# Або так, або так
# from pages.base import HomePage as h
# from pages.base import RegistrationPage as r

driver = webdriver.Chrome()
driver.set_window_position(2000, 600)
driver.maximize_window()
url = 'https://dumskaya.net/'
driver.get(url)
home = base.HomePage(driver)
reg = base.RegistrationPage(driver)

# home.open_articles_page()

# Розібратись чого не працює
# home.open_home_page()
home.user_menu()
home.registration_user()
reg.registration(user_data.email,user_data.nick,user_data.password)

time.sleep(3000)