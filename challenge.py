from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re

s = HTMLSession() 
url = 'https://en.wikipedia.org/wiki/List_of_animal_names'
r = s.get(url)
table = r.html.find('table')[2]

data = [[c.text for c in row.find('td')] for row in table.find('tr')[2:]]

# headers = [[c.text for c in row.find('th')] for row in table.find('tr')[:1]]

print(data[1])
for animal in data:
    # So we can skip each td without data (our table is seperated by letters) 
    if len(animal) < 5:
        continue

    if animal[4] =='—':
        animal[5] = re.sub(r'\[.*?\]', '', animal[5])
        print('###### \n', animal[0], ':', animal[5])

    else:
        animal[4] = re.sub(r'\[.*?\]', '', animal[4])
        print('###### \n', animal[0], ':', animal[4])

