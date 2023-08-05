from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import pandas as pd

website = 'https://gamerant.com/'
path = 'geckodriver.exe'

# active headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Firefox(service=service, options=options)
driver.get(website)

print('Collecting data...')

news_containers = driver.find_elements(by="xpath", value='//div[@class="w-display-card-content"]')
titles = list()
links = list()

for news in news_containers:
    title = news.find_element(by='xpath', value='./h5/a').text
    link = news.find_element(by='xpath', value='./h5/a').get_attribute('href')
    titles.append(title)
    links.append(link)


# export news as .csv file
news_dict = {"Titles": titles, "Links": links}
latest_news = pd.DataFrame(news_dict)
latest_news.to_csv("gamerant.csv")

driver.quit()