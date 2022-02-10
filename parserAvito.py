import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.avito.ru/shops'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0', 'accept': '*/*'}
HOST = 'https://www.avito.ru'
FILE = 'a.csv'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS,  params=params)
    return r

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['company', 'link', 'city'])
        for item in items:
            writer.writerow([item['company'], item['link'], item['city']])

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='t_s_i')

    companies = []

    for item in items:
        city = item.find('div', class_='t_s_items').find_next('span', class_='').find_next('span', class_='').get_text()
        companies.append({
            'company': item.find('a', class_='').get_text(strip = True).replace('\n', ''),
            'link': HOST + item.find('a', class_='').get('href'),
            'city': city,
            })
    return companies

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        companies = get_content(html.text)
        save_file(companies, FILE)
        print(companies)
    else:
        print('none')

parse()