#!python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s =input()
g ='https://www.google.de/search?q=' + s
print(g)
browser =webdriver.Chrome()
browser.get('https://www.google.com/search?q=' + s)
s =browser.find_elements_by_xpath('//*[@id="rso"]')
g =browser.find_elements_by_class_name('r')
for i in range(10):
    print(g[i].text)

