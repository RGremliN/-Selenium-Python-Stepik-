import time
import math
import os 

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
with webdriver.Chrome() as browser:

    browser.get(link)
    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)


    y = calc(browser.find_element(By.CSS_SELECTOR,'#input_value').text)

    browser.find_element(By.CSS_SELECTOR,'#answer').send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()


    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


