from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://select2.org/selections'
try:
        browser = webdriver.Chrome('/Users/ilyich/Downloads/chromedriver')
        browser.get(link)

        # Проверка наличие слов Built-in escaping на странице
        find_word = browser.find_element(By.XPATH, "//h3[@id = 'built-in-escaping']").text
        print(f'Текст в элементе: {find_word}')
        time.sleep(1)

        # Прокрутка страницы к первому select2
        browser.execute_script("window.scrollTo(0, 350);")
        time.sleep(1)

        # Поиск первого select2 и выбор 3-го пункта из выпадающего списка
        browser.find_element(By.XPATH, '//span[@class="select2-selection select2-selection--single"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, "//li[text()= 'California']").click()

        # Screenshot 1
        browser.get_screenshot_as_file('screen_element_1.png')
        time.sleep(1)

        # Прокрутка страницы ко второму select2
        browser.execute_script("window.scrollTo(0, 1700);")
        time.sleep(1)

        # Поиск второго select2 и выбор 2-го пункта из выпадающего списка
        browser.find_element(By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]').click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//li[text()= 'Hawaii']").click()
        time.sleep(2)

        # Screenshot 2
        browser.get_screenshot_as_file('screen_element_2.png')
        time.sleep(1)
finally:
        browser.quit()


