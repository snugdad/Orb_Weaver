import re
import requests
from bs4 import BeautifulSoup


carryDict = ["att", "verizon", "sprint", "t-mobile"]


class iphoneListing:
	default = "(null)"
	def __init__(self, iphoneDict):
		self.model = int(iphoneDict.get("model", 0))
		self.color = str(iphoneDict.get("color", "(null)"))
		self.storage = iphoneDict.get("storage", "(null)")
		self.unlocked = iphoneDict.get("unlocked", "(null)")
		self.gsm = iphoneDict.get("gsm", "(null)")
		self.cdma = iphoneDict.get("cdma", "(null)")
		self.carrier = iphoneDict.get("carrier", "(null)")
		self.link = iphoneDict.get("link", "(null)")
	def printParams(self):
		print("href: %s" % self.link)
		print("Model type: %d" % self.model)
		print("Color: %s" % self.color)
		print("Storage Capacity: ", self.storage)
		print("Unlocked?: %r" % self.unlocked)
		print("GSM radio?: %r" % self.gsm)
		print("CDMA radio?: %r" % self.cdma)
		print("Carrier: %s" % self.carrier)
		print("\n")

def str_is_number_te(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
			
def parseTitle(title, link):
	attrs = title.split('-')
	iphoneDict = {}
	attrlen = len(attrs)
	iphoneDict['link'] = link
	count = 0
	for word in attrs:
		word = word.lower()
		if word == "iphone":
			#print("this title is iphone")
			if count < attrlen and attrs[count + 1].lower() == "x": 
				iphoneDict['model'] = 10
				#print(iphoneDict)
		elif "gb" in attrs[count].lower():
			#print("found storage")
			#if count > 1 and str_is_number_te(attrs[count - 1]) == True:
			iphoneDict['storage'] = re.findall('\d+', word)
		elif word == "gb":
			if str_is_number_te(attrs[count - 1]):
				junklist = re.findall('\d+', word)
				iphoneDict['storage'] = atoi(junklist[0]);
		elif word == "space" or word == "gray" or word == "grey":
			iphoneDict['color'] = "gray"
		elif word == "silver":
			iphoneDict['color'] = "silver"
		elif word == "unlocked":
			iphoneDict['unlocked'] = True
		elif word == "cdma":
			iphoneDict['cdma'] = True
		elif word == "gsm":
			iphoneDict['gsm'] = True
		elif word in carryDict:
			iphoneDict['carrier'] = word
		count += 1
	newListing = iphoneListing(iphoneDict)	
	return newListing
	print("\n")

def getListing(link):
	text_blocks = link.split("/")
	title = text_blocks[4]
	newListing = parseTitle(title, link)
	return(newListing)

def trade_spider(max_pages):
	page = 1
	adList = []
	while page <= max_pages:
		url = 'https://www.ebay.com/sch/15032/i.html?_from=R40&_nkw=iphone+x&_pgn=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, "html.parser")
		for link in soup.find_all('a', {'class': 's-item__link'}):
			href = link.get('href')
			#print(link)
			adList.append(getListing(str(href)))
		page += 1

	for ad in adList:
		ad.printParams()
trade_spider(1)