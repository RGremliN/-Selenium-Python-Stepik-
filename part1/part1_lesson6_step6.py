import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By



# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
with webdriver.Chrome() as browser:

    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector('[type="text"]')
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
