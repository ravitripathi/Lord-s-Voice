import requests as rq
from bs4 import BeautifulSoup
#with open('data.txt') as f:

page = rq.get('https://www.goodreads.com/work/quotes/1492580-bhagavadg-t')

soup = BeautifulSoup(page.text, 'html.parser')

for i in soup.div['class']:
	print i
