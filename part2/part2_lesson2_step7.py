import time
import math
import os 

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
with webdriver.Chrome() as browser:

    browser.get(link)
    time.sleep(1)


    for x in browser.find_elements(By.CSS_SELECTOR, '.form-control[required]'):
        x.send_keys('1')
        pass


    browser.find_element(By.CSS_SELECTOR,'[type="file"]').send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()


    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


