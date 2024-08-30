import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
url = "https://www.basketball-reference.com/"
r = requests.get(url)
soup = BS(r.text, 'html.parser')
rows = soup.find('table',{"id":"wnba_standings"}).find('tbody').find_all('tr')

team_list = []

for row in rows:
    dic = {}

    dic['W'] = row.find_all('td')[0].text
    dic['team'] = row.find_all('th')[0].text
    dic['L'] = row.find_all('td')[1].text
    dic['W/L'] = row.find_all('td')[2].text
    dic['GB'] = row.find_all('td')[3].text
    team_list.append(dic)

    df = pd.DataFrame(team_list)
    df.to_csv('team_data.csv', index=False)

print(team_list)
















