def registration(email, nick, password):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    import xpath_dumskaya as x
    import user_data

    driver = webdriver.Chrome()
    driver.set_window_position(2000, 600)
    driver.maximize_window()
    url = 'https://dumskaya.net/'
    driver.get(url)
    # https://selenium-python.readthedocs.io/waits.html
    # https://www.selenium.dev/documentation/webdriver/waits/

    # element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "myDynamicElement"))
    enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.enter_button)))
    enter_button.click()

    registration_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, x.registration_button)))
    registration_button.click()

    email_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.email_field)))
    email_field.send_keys(email)

    nick_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.nick_field)))
    nick_field.send_keys(nick)

    password_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.password_field)))
    password_field.send_keys(password)

    password2_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.password2_field)))
    password2_field.send_keys(password)

    male_radio = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.male_radio)))
    male_radio.click()

    finish_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.finish_button)))
    finish_button.click()

    user_name_label = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.user_name_label)))

    return user_name_label.text
