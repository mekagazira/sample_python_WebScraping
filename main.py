from selenium import webdriver
from time import sleep

# 参照先ページ
url = "https://www.nifty.com/"

# ブラウザ起動・ページ表示
browser = webdriver.Chrome("chromedriver.exe")
browser.get(url)

# 一時停止
sleep(1)

# 検索ワードを入力
element_search_txt = browser.find_element_by_id("srchTxt")
element_search_txt.send_keys("ほげほげ")

# 一時停止
sleep(1)

# 検索ボタン押下
element_search_btn = browser.find_element_by_id("srchBtn")
element_search_btn.click()

# 一時停止
sleep(1)

# ブラウザ停止
browser.quit()