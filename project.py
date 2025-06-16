from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


driver = webdriver.Chrome(options=options)

query = "laptop"
file = 0

output_folder = f"data"
os.makedirs(output_folder, exist_ok=True)

for i in range(1,20) :
    print(f"Fetching page {i}...")
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=13LY6V3ENLKJD&sprefix=laptop%2Caps%2C236&ref=nb_sb_noss_2")
    
    time.sleep(3) #let the page fully load, enabling more human like 

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found on page {i}")
    
    for elem in elems :
        d = elem.get_attribute("outerHTML")
        with open(f"{output_folder}/{query}_{file}.html", "w", encoding="utf-8") as f :
            f.write(d)
            file += 1
    
    time.sleep(4)

driver.quit()