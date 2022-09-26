from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:/Users/Asanka/Desktop/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Running cookie clicker for 5 minutes

t_end = time.time() + 60*5
while time.time() < t_end:

    #Keep clicking repeatedly for 5 seconds

    t_click = time.time() + 5
    while time.time() < t_click:
        cookie = driver.find_element(By.XPATH, "//*[@id='cookie']")
        cookie.click()
    
    #After 5 seconds, record cookie amount and price of items in the store.

    cookie_amount = int(driver.find_element(By.ID, "money").text.replace(',',''))
    cursor = int((driver.find_element(By.ID,"buyCursor").text.split()[2].replace(',','')))
    grandma = int((driver.find_element(By.ID,"buyGrandma").text.split()[2].replace(',','')))
    factory = int((driver.find_element(By.ID,"buyFactory").text.split()[2].replace(',','')))
    mine = int((driver.find_element(By.ID,"buyMine").text.split()[2].replace(',','')))
    shipment = int((driver.find_element(By.ID,"buyShipment").text.split()[2].replace(',','')))
    alchemy = int((driver.find_element(By.ID,"buyAlchemy lab").text.split()[3].replace(',','')))
    portal = int((driver.find_element(By.ID,"buyPortal").text.split()[2].replace(',','')))
    time_machine = int((driver.find_element(By.ID,"buyTime machine").text.split()[3].replace(',','')))

    store = {
        "buyCursor" : cursor,
        "buyGrandma": grandma,
        "buyFactory" : factory,
        "buyMine" : mine,
        "buyShipment" : shipment,
        "buyAlchemy lab" : alchemy,
        "buyPortal" : portal,
        "buyTime machine" : time_machine
    }

    #Find out the most expensive item in the store, and locate its position in the browser.

    for item in store:
        if cookie_amount > store[item]:
            location = driver.find_element(By.ID, item)

    #Click the item in the browser store.

    location.click()

#At the end of 5 minutes, records the rate at which cookies are produced.   

rate = driver.find_element(By.ID, "cps").text
print(rate)


time.sleep(10)


