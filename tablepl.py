import requests
from bs4 import BeautifulSoup

url = 'https://www.skysports.com/premier-league-table'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')
for row in rows:
    data = []
    for head in row.find_all('th'):
        heads = head.text
        data.append(heads)
    for body in row.find_all('td')[:10]:
        bodies = body.text.replace('\n', '')
        data.append(bodies)

    print(data)