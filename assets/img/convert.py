from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:

    driver.get("file:///Users/yao/respo/llmvdb.github.io/index.html") 

    element = driver.find_element(By.TAG_NAME, 'svg') 

    element.screenshot("/Users/yao/respo/llmvdb.github.io/assets/img/logo.jpg")
    
finally:

    driver.quit()
