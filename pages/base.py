from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import xpath_dumskaya as x
import user_data


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def register_new_user(self):
        enter_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//a[@id="pp"]/b')))
        enter_button.click()
        registration_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/register/"]')))
        registration_button.click()

    def user_menu(self):
        enter_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//a[@id="pp"]/b')))
        enter_button.click()

    def registration_user(self):
        registration_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/register/"]')))
        registration_button.click()

    def open_home_page(self):
        logo_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="logocell"]')))
        logo_button.click()

    def open_articles_page(self):
        articles_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="menutable"]/div/a[@href="/articles/"]')))
        articles_button.click()

    def open_top_page(self):
        top_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="menutable"]/div/a[@href="/topweek/"]')))
        top_button.click()


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        pass

    def registration(self, email, nick, password):
        email_field = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, x.email_field)))
        email_field.send_keys(email)

        nick_field = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, x.nick_field)))
        nick_field.send_keys(nick)

        password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, x.password_field)))
        password_field.send_keys(password)

        password2_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, x.password2_field)))
        password2_field.send_keys(password)

        male_radio = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, x.male_radio)))
        male_radio.click()

        finish_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, x.finish_button)))
        finish_button.click()


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        pass

class TopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        pass

    def first_line(self):
        first_news = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="content"]/table/tbody/tr/td[@valign="top" and not(@class="newsdatetd2")]/a')))
        return first_news.text