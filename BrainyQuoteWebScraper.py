from bs4 import BeautifulSoup
from urllib2 import urlopen, Request, HTTPError
from json import dump
import sys


AUTHOR = str(sys.argv[1])
NUM_PAGES = int(sys.argv[2])

BASE_URL = 'http://www.brainyquote.com/quotes/authors/' + AUTHOR[0] + '/' + AUTHOR + '_'
#BASE_URL = 'http://www.brainyquote.com/quotes/authors/c/christopher_hitchens_'
#TEST_URL = 'http://www.brainyquote.com/quotes/quotes/c/christophe472395.html'
LXML_PARSER = 'lxml'
HEADERS = {'User-Agent' : 'Mozilla/5.0'}


def make_soup(url):
	req = Request(url, headers=HEADERS)
	html =urlopen(req).read()
	return BeautifulSoup(html, LXML_PARSER)


# try:
# 	soup = make_soup(TEST_URL)
# 	#quotes = soup.find('masonryitem boxy bqQt bqShare masonry-brick','bqQuote')
# except HTTPError, e:
# 	print e.fp.read()

#finds quote text
#print soup.find('p','qt_472395').string

def get_quote_numbers():
	quote_numbers = {}
	#NUM_PAGES = 7
	CLASS = 'bqQuoteLink'
	for x in range(1, NUM_PAGES+1):
		soup = make_soup(BASE_URL + str(x) + '.html')
		numbers = [q.next_element.string for q in soup.findAll('span', CLASS)]
		quote_numbers[x] = numbers
	return quote_numbers

def write_to_file():
	quote_dict = get_quote_numbers()
	f = open('quotes.json', 'w+')
	dump(quote_dict, f)
	f.close()

write_to_file();

