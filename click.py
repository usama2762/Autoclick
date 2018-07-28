from selenium import webdriver
try:
	driver = webdriver.Chrome(executable_path=r"C:\new\chromedriver.exe")
    #driver = webdriver.Chrome(executable_path=r"C:\new\chromedriver.exe")
except ValueError:
	try:
		driver = webdriver.Chrome(executable_path=r"C:\new\chromedriver.exe")
	driver.get('http://www.adidas.com/us/tubular-doom-shoes/S74791.html')
submit_button_click = driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[5]').click()