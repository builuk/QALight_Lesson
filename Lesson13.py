def registration(success=True, email='', nick='', password=''):
    from selenium import webdriver
    import time
    from helper.xpath import dumskaya as x
    from helper.waiters import parts

    driver = webdriver.Chrome()
    driver.set_window_position(2000, 600)
    driver.maximize_window()
    url = 'https://dumskaya.net/'

    driver.get(url)
    parts.base_button(driver, x.Home.enter_button)
    parts.base_button(driver, x.Home.registration_button)
    parts.base_field(driver, x.Registration.email_field, email)
    parts.base_field(driver, x.Registration.nick_field, nick)
    parts.base_field(driver, x.Registration.password_field, password)
    parts.base_field(driver, x.Registration.password2_field, password)
    parts.base_button(driver, x.Registration.male_radio)
    parts.base_button(driver, x.Registration.finish_button)
    if success:
        return parts.base_label(driver, x.UserInfo.user_name_label)
    else:
        return parts.base_label(driver, x.Registration.error_label)
