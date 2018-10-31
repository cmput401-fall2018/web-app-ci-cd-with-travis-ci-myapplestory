from selenium import webdriver




# put your own path to chromedriver
chrome_driver_binary = r"/mnt/c/Users/James/Downloads/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_binary)
driver.get("http://162.246.157.231:8000")




def test_home():
    nameElem    = driver.find_element_by_id("name")
    aboutElem   = driver.find_element_by_id("about")
    skillsElem  = driver.find_element_by_id("skills")
    eduElem     = driver.find_element_by_id("education")
    workXPElem  = driver.find_element_by_id("work")
    contactElem = driver.find_element_by_id("contact")

    assert nameElem != None
    assert aboutElem != None
    assert skillsElem != None
    assert eduElem != None
    assert workXPElem != None
    assert contactElem != None

    
test_home()
