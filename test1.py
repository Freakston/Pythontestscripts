#! python3
import requests ,sys
from bs4 import BeautifulSoup

sys.argv
searchterm=' '.join(sys.argv[1:])

site='https://www.google.com/search?q=' + searchterm
print(site)
r = requests.get(site)

soup = BeautifulSoup(r.content, 'html5lib')
soup.select('#rso > div:nth-child(5) > div > div > div > h3 > a')
elem = soup.select
lol = elem[0].text
print(lol)

