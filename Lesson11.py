from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.set_window_position(2000, 600)

driver.maximize_window()

url = 'https://bank.gov.ua/ua/markets/exchangerates'

driver.get(url)

# 1
xpath_name_usd = '//td[contains(text(), "USD")]/parent::tr/td[@class="value-name"]/a'
xpath_value_usd = '//td[contains(text(), "USD")]/parent::tr/td[5]'

usd_name = driver.find_element('xpath', xpath_name_usd)
usd_value = driver.find_element('xpath', xpath_value_usd)
print(usd_name.text, usd_value.text)

# 2

v = ['USD', 'EUR', 'JPY']
for elem in v:
    xpath_name = f'//td[contains(text(), "{elem}")]/parent::tr/td[@class="value-name"]/a'
    xpath_value = f'//td[contains(text(), "{elem}")]/parent::tr/td[5]'
    elem_name = driver.find_element('xpath', xpath_name)
    elem_value = driver.find_element('xpath', xpath_value)
    print(elem_name.text, elem_value.text)

# 3
xpath_names = f'//td[contains(text(), "")]/parent::tr/td[@class="value-name"]/a[contains(text(), "                   ")]'
xpath_values = f'//td[contains(text(), "")]/parent::tr/td[contains(text(), ",")]'
elem_names = driver.find_elements('xpath', xpath_names)

d = []
for elem in elem_names:
    d.append(elem.text)

e = []
elem_values = driver.find_elements('xpath', xpath_values)
for elem in elem_values:
    e.append(elem.text)

t = {}
for i in range(len(d)):
    t[d[i]] = e[i]

for name, value in t.items():
    print(name, value)
time.sleep(300)
