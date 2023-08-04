from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

website = 'https://gamerant.com/'
path = 'geckodriver.exe'

#active headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Firefox(service=service, options=options)
driver.get(website)

news_containers = driver.find_elements(by="xpath", value='//div[@class="w-display-card-content"]')

categories = list()
titles = list()
links = list()

for news in news_containers:
    category = news.find_element(by='xpath', value='//div[@class="w-display-card-content"]\n'
                                                   '//div[@class="w-display-card-category"]/a').text
    title = news.find_element(by='xpath', value='./h5/a').text
    link = news.find_element(by='xpath', value='./h5/a').get_attribute('href')

    categories.append(category)
    titles.append(title)
    links.append(link)

news_dict = {"Categories": categories, "Titles": titles, "Links": links}

recent_news = pd.DataFrame(news_dict)
recent_news.to_csv("gamerant.csv")

print("Process: Collecting news data....")

driver.quit()
