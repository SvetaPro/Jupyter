import requests
from bs4 import BeautifulSoup

url = "http://www.cbr.ru/scripts/XML_daily.asp"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
print(soup)

lst = soup.find_all('name')

for item in lst:
    print(item)
    
url = "https://seaborn.pydata.org/examples/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
# ~ print(soup.prettify())

lst = soup.find_all('p')
del lst[0]
del lst[-1]

for item in lst:
    print(item)
    
def clean_item(my_item):
    position = my_item.find('</p')
    return my_item[4:position]

print("")

for item in lst:
    print(clean_item(str(item)))
