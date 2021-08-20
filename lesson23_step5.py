from selenium import webdriver
import time
import os
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_class_name("trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    sl1 = browser.find_element_by_id('input_value').text
    sl2 = int(sl1)
    y = str(calc(sl2))
    inp_1 = browser.find_element_by_id("answer")
    inp_1.send_keys(y)
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла