import time
import math
import os 

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 

link = "http://suninjuly.github.io/explicit_wait2.html"
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
with webdriver.Chrome() as browser:

    # browser.implicitly_wait(15)
    browser.get(link)


    button = browser.find_element_by_id("book")

    text = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button.click()


    # browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()

    # new_window = browser.window_handles[1]

    # browser.switch_to.window(new_window)


    y = calc(browser.find_element(By.CSS_SELECTOR,'#input_value').text)

    browser.find_element(By.CSS_SELECTOR,'#answer').send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()


    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


