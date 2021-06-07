from selenium import webdriver
from time import sleep


# ブラウザ起動
browser = webdriver.Chrome("chromedriver.exe")

# 一時停止
sleep(3)

# ブラウザ停止
browser.quit()

