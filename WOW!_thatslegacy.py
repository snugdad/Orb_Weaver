"""
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
"""