import requests
from bs4 import BeautifulSoup as soup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0",
           }

url = "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-81.71008420759614%2C%22east%22%3A-81.09004331404145%2C%22south%22%3A28.41963130408765%2C%22north%22%3A28.688625119128112%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22max%22%3A400000%7D%2C%22mp%22%3A%7B%22max%22%3A1980%7D%2C%22beds%22%3A%7B%22min%22%3A4%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22parks%22%3A%7B%22min%22%3A2%7D%2C%22sqft%22%3A%7B%22min%22%3A1500%7D%2C%2255plus%22%3A%7B%22value%22%3A%22e%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22customRegionId%22%3A%22a688964629X1-CR1fhlvldzbu75x_1745vt%22%2C%22pagination%22%3A%7B%7D%2C%22mapZoom%22%3A11%7D"

html = requests.get(url=url, headers=headers)
print(html.status_code)

bsobj = soup(html.content, 'lxml')

price_list = []
for price in bsobj.findAll('div',{'class':'list-card-heading'}):
    price_list.append(price.text.replace('bd','b|').replace('|s','|').replace('o','o|').strip().split('|')[:-1])
print("price_list:")
print(price_list)

address = []
for adr in bsobj.findAll('div', {'class':'list-card-info'}):
    address.append(adr.a.text.strip())
print("address:")
print(address)
