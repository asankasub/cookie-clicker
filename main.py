from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.python.org/')

# n = driver.find_element(by=By.NAME, value="q")
# n = driver.find_element(by=By.CLASS_NAME, value="python-logo")
# n = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
# print(n.text)
# n = driver.find_element(by=By.XPATH, value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(n.text)
# driver.find_elements

# date = driver.find_element(by=By.XPATH, value="//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[1]/time")
# title = driver.find_element(by=By.XPATH, value="//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[1]/a")
# print(title.text)

# dict={}


for i in range(1,6):
    date = driver.find_element(by=By.XPATH, value=f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]/time")
    title = driver.find_element(by=By.XPATH, value=f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]/a")
    
    dict[i-1] = {"time" : f"2022-{date.text}",
        "name" : title.text}
print(dict)

