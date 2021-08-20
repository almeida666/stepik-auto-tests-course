from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id('book')
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button.click()
    s1 = browser.find_element_by_id('input_value').text
    y = str(calc(int(s1)))
    in1 = browser.find_element_by_id('answer')
    in1.send_keys(y)
    button2 = browser.find_element_by_id('solve')
    button2.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла