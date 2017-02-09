import requests as rq
from bs4 import BeautifulSoup
import codecs
#with open('data.txt') as f:

url = 'https://www.goodreads.com/work/quotes/1492580-bhagavadg-t'
n = "?page=2"
page = rq.get(url)
data = []
soup = BeautifulSoup(page.text, 'html.parser')

for i in range(2, 7):
	for j in soup.find_all("div", class_="quoteText"):
		data.append(j.contents[0])
	page = rq.get(url + "?page=" + str(i))
	soup = BeautifulSoup(page.text, 'html.parser')
	print "Completed page" + str(i-1)

with codecs.open('data.txt', 'w', 'utf-8') as f:
	for k in data:
		f.write(k)

print "Completed!"
