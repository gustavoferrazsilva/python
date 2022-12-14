from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


WP_LINK = 'https://web.whatsapp.com'

driver = webdriver.Chrome()
driver.get(WP_LINK)
while True:
    sleep(20)
    break