import requests
from bs4 import BeautifulSoup
import csv
import datetime

# connect to web data with page
link = "https://www.webometrics.info/en/world?page="

datas = []
for page in range(0, 121):
    req = requests.get(link + str(page))
    soup = BeautifulSoup(req.text, 'html.parser')
    univ = soup.findAll('tr', ['odd', 'even'])
    for un in univ:
        date_today = datetime.date.today()
        rank = un.find(['td', 'center']).text
        linkuniv = un.find('a')['href'].replace(
            'https://', '').replace('http://', '').replace('/', '')
        name = un.find('a').text
        country = (un.find('img', alt='bandera')['src']
                   .replace('https://www.webometrics.info/sites/default/files/logos/', '')
                   .replace('.png', ''))
        #piccountry = un.find('img',alt ='bandera')['src']
        # print(rank,name,linkuniv,country,piccountry)
        datas.append([date_today, name, rank, linkuniv, country])

header = ['Date_scrape', 'Name', 'Rank', 'Url', 'Country']

# open the file in the write mode
with open('univdat.csv', 'w', encoding='UTF8', newline='') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(header)
    for n in datas:
        writer.writerow(n)
