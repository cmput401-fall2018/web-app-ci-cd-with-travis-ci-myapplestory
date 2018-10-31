from selenium import webdriver


# put your own path to chromedriver
chrome_driver_binary = r"/mnt/c/Users/James/Downloads/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_binary)
driver.get("http://162.246.157.231:8000")

elem = driver.find_element_by_id("name")
print(elem)


