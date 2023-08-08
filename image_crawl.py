"""
Crawl Images from websites
"""
from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
from tqdm import tqdm
import os

driver = webdriver.Chrome()
driver.get("https://www.shutterstock.com/ko/search/%EC%95%88%EA%B2%BD?mreleased=true")

# search = "people wearing glasses"
# elem = driver.find_element(By.NAME,"q")
# elem.send_keys(search)
# elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR,".MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeLarge MuiButton-outlinedSizeLarge MuiButton-disableElevation MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeLarge MuiButton-outlinedSizeLarge MuiButton-disableElevation mui-l1ws68-a-inherit").click()
        except:
            break
    last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR,".mui-t7xql4-a-inherit-link")
count = 1

for image in tqdm(images):
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element(By.XPATH,'//*[@id="__next"]/div[3]/div/div[2]/div[1]/div/div[5]/div[1]/div[2]/div[1]/a').get_attribute('src')
        urllib.request.urlretrieve(imgUrl, "people_wearing_glasses/" + "people_wearing_glasses_" + str(count) + ".jpg")
        print("Image saved: crawl_{}.jpg".format(count))
        count += 1
    except:
        pass

driver.close()
