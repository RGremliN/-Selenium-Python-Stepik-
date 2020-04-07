import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver



# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(20)

# Ищем кнопку для открытия окна авторизации
auth_button = driver.find_element_by_css_selector(".navbar__auth_type_login")
time.sleep(5)

# Кликаем на кнопку
auth_button.click()
time.sleep(5)

# Здесь использую метод find_element_by_name
# Ищем поле для логина и вводим его
login = driver.find_element_by_name("login")
login.send_keys("zendesar@gmail.com")

# Ищем поле для пароля и вводим его
password = driver.find_element_by_name("password")
password.send_keys("33e9dec")

sign_in_button = driver.find_element_by_css_selector(".sign-form__btn")
time.sleep(5)

sign_in_button.click()
time.sleep(20)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
