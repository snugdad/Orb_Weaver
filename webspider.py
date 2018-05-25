import re
import requests
from bs4 import BeautifulSoup


"""
def get_model(s_model):
	



class iphoneListing:
	def __init__(self, s_model, s_storage_sz, s_unlocked, s_carrier, s_radio_type, s_condition):
		self.model = get_model(s_model)
"""
def str_is_number_te(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
			
def parseTitle(title):
	attrs = title.split("-")
	iphone_dict = {}
	count = 0
	for word in attrs:
		if "iphone" in word.lower():
			print("this title is iphone")
			print(title)
			if attrs[count + 1].lower() == "x": 
				print ("Found an X model")
				iphone_dict['model'] = 10
				print("\n")
				print(iphone_dict)
		elif "gb" in word.lower():
			if count > 1 && str_is_number_te(attrs[count - 1]) == True:
			iphone_dict['storage'] = re.findall('\d+', word)
			print(iphone_dict)
		count += 1
	print ("\n")

def getTitle(link):
	text_blocks = link.split("/")
	title = text_blocks[4]
	parseTitle(title)
	return(title)

def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'https://www.ebay.com/sch/15032/i.html?_from=R40&_nkw=iphone+x&_pgn=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, "html.parser")
		for link in soup.find_all('a', {'class': 's-item__link'}):
			href = link.get('href')
			#print(href);
			title = getTitle(str(link))
		page +=1

trade_spider(1)