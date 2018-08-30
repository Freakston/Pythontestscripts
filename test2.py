Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> from bs4 import BeautifulSoup
>>> searchterm ='Bigbang'
>>> site='https://www.google.com/search?q=' + searchterm
>>> print(site)
https://www.google.com/search?q=Bigbang
>>> r=get9site)
SyntaxError: invalid syntax
>>> r=get(site)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    r=get(site)
NameError: name 'get' is not defined
>>> r=requests.get(site)
>>> soup=BeautifulSoup(r.content, 'html.parser')
>>> soup.select('#rso > div:nth-child(2) > div > div > g-section-with-header > div.e2BEnf > div > h3 > g-link > a')
[]
>>> soup.select('#rso > div:nth-child(2) > div > div > g-section-with-header > div.e2BEnf > div > h3 > g-link')
[]
>>> shit = soup.find('div', class_='otisdd')
>>> for link in shit.select('div.title a[href]'):
	print link['href']
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(link['href'])?
>>> print(link['href'])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(link['href'])
NameError: name 'link' is not defined
>>> print link['href']
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(link['href'])?
>>> print (link['href'])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print (link['href'])
NameError: name 'link' is not defined
>>> for link in shit.select('div.title a[href]'):
	print(link['href'])

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    for link in shit.select('div.title a[href]'):
AttributeError: 'NoneType' object has no attribute 'select'
>>> 
