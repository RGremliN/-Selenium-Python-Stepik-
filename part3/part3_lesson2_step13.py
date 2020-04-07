import time
import math
import unittest


# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By
 

class TestReg(unittest.TestCase):

    def test_page1(self):

        with webdriver.Chrome() as browser:

            browser.implicitly_wait(5)

            browser.get("http://suninjuly.github.io/registration1.html")

            input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
            input3.send_keys("aa@aa.aa")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"{welcome_text} not equal welcome text")

            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_page2(self):

        with webdriver.Chrome() as browser:

            browser.implicitly_wait(5)

            browser.get("http://suninjuly.github.io/registration2.html")

            input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
            input3.send_keys("aa@aa.aa")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"{welcome_text} not equal welcome text")

            # закрываем браузер после всех манипуляций
            browser.quit()




#запускаем тесты
if __name__ == "__main__":
    unittest.main()

# не забываем оставить пустую строку в конце файла
