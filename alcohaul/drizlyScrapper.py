import urllib2
from bs4 import BeautifulSoup
import pandas as pd

import urllib

#specify the url
beerAle = "https://drizly.com/search?cid%5B%5D=2&cid%5B%5D=196812&page=2"

individualDrink = "https://drizly.com/stella-artois/p4868"

#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(beerAle)

soup = BeautifulSoup(page, "html.parser")
#all_tables=soup.find_all('section')

right_table=soup.find('section', class_='section-body list-view ')


Name = ""
Price = 0

for row in right_table.find_all('li') :
	for data in row.find_all('p'):
	#	print data.string.strip()
		if str(data).count('$')==0:
			Name = data.string.strip()
		"""
		if str(data).count('$')==0:

			Name = str(data).split('$')[1][0:-4]
	"""
	for data2 in row.find_all('img'):
		imageData = str(data2)
		imageURL = "http://"+imageData.split(' ')[-1][7:-3]
		imageName = imageData.split('"')[1]
		urllib.urlretrieve(imageURL, imageName+".jpg")
		Price = imageData.split('"')[17]
	#	print price,"$$$$$$$"

		print "a = alcohol(name = "+'"'+Name+'"'+ ", price = "+Price+",quantity="+ "100" +   ")"
		print "a.save()"
	
