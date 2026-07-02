import requests
from bs4 import BeautifulSoup

site = "https://www.nasa.gov"

r = requests.get(site)

print(r.status_code)


soup = BeautifulSoup(r.content,"html.parser")
pretty_soup = soup.prettify()

print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)

#for link in soup.find_all('a'):
#    print(link.get('href'))

print(soup.get_text())

