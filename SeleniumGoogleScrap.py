import time

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
try:
    toutAccepter=driver.find_element(By.ID,"L2AGLb")
    toutAccepter.click()
except:pass
searchBox=driver.find_element(By.NAME,"q")
searchBox.send_keys("Maroc")
searchBox.send_keys(Keys.ENTER)
WebDriverWait(driver,15).until(EC.presence_of_element_located((By.TAG_NAME,"h3")))

for i in range(1,1):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)

blocs=driver.find_elements(By.CSS_SELECTOR,'span[jscontroller="msmzHf"]')

for bloc in blocs:
    if bloc.text.strip()!="":
        try:
            titre=bloc.find_element(By.TAG_NAME,"h3").text
            lien=bloc.find_element(By.TAG_NAME,"a").get_attribute("href")
            print(titre)
            print(lien)
            print("----------------------------------------------------------------------")
        except: continue