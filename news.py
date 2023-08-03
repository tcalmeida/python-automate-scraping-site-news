from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import pandas as pd

website = "https://gamerant.com/"
path = "geckodriver.exe"

service = Service(executable_path=path)
driver = webdriver.Firefox(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="w-display-card-content"]')

categories = list()
titles = []
links = []

for container in containers:

    title = container.find_element(by='xpath', value='./h5/a').text
    link = container.find_element(by='xpath', value='./h5/a').get_attribute('href')

    titles.append(title)
    links.append(link)

news_dict = {"title": titles, "links": links}

recent_news = pd.DataFrame(news_dict)
recent_news.to_csv("recent_news.csv")

print("Process: Collecting news data....")

driver.quit()
