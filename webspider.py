import re
import requests
from bs4 import BeautifulSoup


carrierDict = ["att", "verizon", "sprint", "t-mobile"]

class phoneCaseListing:
	def __init__(self, title):
		if "disney" in title:
			self.theme = "disney"
		elif "universal" in title:
			self.theme = "universal"
		def printParams(self):
			print("Theme of case: %s" % self.theme)

class phoneListing:
	def __init__(self, phoneDict):
		self.title = str(phoneDict.get("title", ("(no title)")))
		self.make = str(phoneDict.get("make", 0))
		self.model = int(phoneDict.get("model", 0))
		self.color = str(phoneDict.get("color", 0))
		self.storage = str(phoneDict.get("storage", 0))
		self.unlocked = phoneDict.get("unlocked", False)
		self.gsm = phoneDict.get("gsm", False)
		self.cdma = phoneDict.get("cdma", False)
		self.carrier = phoneDict.get("carrier", "unknown")
		self.link = phoneDict.get("href", 0)
		if "case" in phoneDict.keys():
			self.case = phoneCaseListing(self.title)
	def printParams(self):
		if self.model != 0:
			print("href: %s" % self.link)
			print("title: %s" % self.title)
			print("Make of phone: %s" % self.make)
			print("Model type: %d" % self.model)
			print("Color: %s" % self.color)
			print("Storage Capacity: %sGB" % self.storage)
			print("Unlocked?: %r" % self.unlocked)
			print("GSM radio?: %r" % self.gsm)
			print("CDMA radio?: %r" % self.cdma)
			print("Carrier: %s" % self.carrier)
			print("Case specifications: %s" % self.case.theme)
			print("\n")
def is_numeric(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def parseTitle(title, link):
	title = title.lower()
	phoneDict = {}
	phoneDict['href'] = link
	phoneDict['title'] = title
	
	if "iphone" and "-x-" in title:
		phoneDict['make'] = 'iphone'
		phoneDict['model'] = 10
	elif "iphone" and "-10-" in title:
		phoneDict['make'] = 'iphone'
		phoneDict['model'] = 1
	if "gb" in title:
		loc = title.find("gb")
		while title[loc - 1] == '-':
			loc -= 1
		count = loc	
		while is_numeric(title[count - 1]):
			count -= 1
		phoneDict['storage'] = title[count:loc]
	if "case" in title:
		phoneDict['case'] = True
	if "space" or "gray" or "grey" in title:
		phoneDict['color'] = 'gray'
	if "silver" in title:
		phoneDict['color'] = 'silver'
	if "unlocked" in title:
		phoneDict['unlocked'] = True
	if "gsm" in title:
		phoneDict['gsm'] = True
	if "cdma" in title:
		phoneDict['cdma'] = True
	for entry in carrierDict:
		if entry in title:
			phoneDict['carrier'] = entry
	newListing = phoneListing(phoneDict)
	return newListing		


def getListing(link):
	text_blocks = link.split("/")
	title = text_blocks[4]
	newListing = parseTitle(title, link)
	return(newListing)

def trade_spider(max_pages):
	page = 1
	adList = []
	while page <= max_pages:
		url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xiphone.TRS0&_nkw=iphone&_sacat=' + str(page)
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