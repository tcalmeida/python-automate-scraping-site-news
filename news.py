from selenium import webdriver
from selenium.webdriver.firefox.service import Service

website = "https://www.gamespot.com/"
path = "geckodriver.exe"

service = Service(executable_path=path)
driver = webdriver.Firefox(service=service)
driver.get(website)