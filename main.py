import re
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from html_sanitizer import Sanitizer

class Listing:
    def __init__(self, address, price, bds, bas, sqft) -> None:
        self.address = address
        self.price = price
        self.bds = bds
        self.bas = bas
        self.sqft = sqft

    def pretty_address(self, address):
        address = listing.findAll('address')
        address = sanitizer.sanitize(str(address))
        address = address[1:-1]
        print(f'Address: {address}')

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0",
           }
url = "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-81.71008420759614%2C%22east%22%3A-81.09004331404145%2C%22south%22%3A28.41963130408765%2C%22north%22%3A28.688625119128112%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22max%22%3A400000%7D%2C%22mp%22%3A%7B%22max%22%3A1980%7D%2C%22beds%22%3A%7B%22min%22%3A4%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22parks%22%3A%7B%22min%22%3A2%7D%2C%22sqft%22%3A%7B%22min%22%3A1500%7D%2C%2255plus%22%3A%7B%22value%22%3A%22e%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22customRegionId%22%3A%22a688964629X1-CR1fhlvldzbu75x_1745vt%22%2C%22pagination%22%3A%7B%7D%2C%22mapZoom%22%3A11%7D"

html = requests.get(url=url, headers=headers)
#print(f'html.context:\n\n{html.content}\n\n')
soup = BeautifulSoup(html.content, 'lxml')
#print(f'pretty: \n\n{soup.prettify()}\n\n')
tags = soup.find_all(id="grid-search-results")
#print(f'tags:\n\n{tags}\n\n')

ListingsArray = []
sanitizer = Sanitizer({
    'tags': ('h1', 'h2', 'p'),
    'attributes': {},
    'empty': set(),
    'separate': set(),
})

print(f'\n***************listings***************\n')
for i, listing in enumerate(soup.findAll('div',{'class':'property-card-data'})):
    print(f'listing {i+1}')
    address = listing.findAll('address')
    address = sanitizer.sanitize(str(address))
    address = address[1:-1]
    print(f'Address: {address}')

    house_price = listing.findAll('span')
    house_price = sanitizer.sanitize(str(house_price))
    house_price = house_price[1:-1]
    print(f'House price: {house_price}')

    bedrooms = listing.findAll('li')
    nested_vars = []
    for num in bedrooms:
        num = sanitizer.sanitize(str(num))
        nested_vars.append(num)
        print(f'\t{num}')
    
    print('\n')
    listing_temp = Listing(address=address, price=house_price, bds=nested_vars[0], 
                           bas=nested_vars[1], sqft=nested_vars[2])
    ListingsArray.append(listing_temp)

for listing in ListingsArray:
    print(f'Addr:\t{listing.address}\n' 
          f'Price:\t{listing.price}\n'
          f'Beds:\t{listing.bds}\n'
          f'Baths:\t{listing.bas}\n'
          f'Sqft:\t{listing.sqft}\n')


# with open('output.txt', 'a') as f:
#     f.write(price)
#print('price is: ', price.text.replace('bd','b|').replace('|s','|').replace('o','o|').strip().split('|')[:-1])
#print(price_list)

# print("address:")
# address = []
# for adr in bsobj.findAll('div', {'class':'property-card-data'}):
#     address.append(adr.a.text.strip())
# print(address)


# df = pd.DataFrame(price_list, columns=['Address','City','State','Price','Sqft','Status'])

# #df['Address'] = address
# print(df)
