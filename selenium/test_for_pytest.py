from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

import time

browser = webdriver.Chrome('/Users/ilyich/Downloads/chromedriver')
link = 'https://select2.org/selections'

def test_main_search():
    global browser
    try:
        """ Проверка текста Built-in escaping на странице """
        text = 'Built-in escaping'
        browser.get(link)
        find_word = browser.find_element(By.XPATH, "//h3[@id = 'built-in-escaping']").text
        time.sleep(1)
        assert text == find_word, 'FAILED (Текст не соответствует тексту в элементе)'

        """ Прокрутка страницы к первому select2 """
        browser.execute_script("window.scrollTo(0, 350);")
        time.sleep(1)

        """ Поиск первого select2 и выбор 3-го пункта из выпадающего списка """
        browser.find_element(By.XPATH, '//span[@class="select2-selection select2-selection--single"]').click()
        find_select2 = browser.find_element(By.XPATH, "//li[text()='California']")
        find_select2.click()
        assert find_select2, 'Отсутствует select2, пункт 3'
        time.sleep(2)

        """ Screenshot 1 """
        browser.get_screenshot_as_file('screen_element_1.png')
        time.sleep(1)

        """ Прокрутка страницы ко второму select2 """
        browser.execute_script("window.scrollTo(0, 1700);")
        time.sleep(1)

        """ Поиск второго select2 и выбор 2-го пункта из выпадающего списка """
        browser.find_element(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').click()
        select2_1 = browser.find_element(By.XPATH, "//li[text()='Hawaii']")
        select2_1.click()
        assert select2_1, 'Отсутствует select2, пункт 2'
        time.sleep(2)

        """ Screenshot 2 """
        browser.get_screenshot_as_file('screen_element_2.png')
        time.sleep(1)
    finally:
        browser.quit()

