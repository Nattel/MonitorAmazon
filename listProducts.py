import requests
from datetime import datetime
from bs4 import BeautifulSoup
import re

class GetSite():
	def __init__(self, url):
		s = requests.session()
		r = s.get(url)

		self.soup = BeautifulSoup(r.text, 'html.parser')

	def listBooks(self):
		# aims first for the 'center' div where the books are and then enlists them
		divs = self.soup.find('div', {'id': 'content-right'}).find('div', {'id': 'item-page-wrapper'})
		self.lis = divs.find('ul').findAll('li')

		return self.lis

	def getsBookInfo(self, li):
		authorInfo = li.find('span', {'class': 'a-size-base'}).getText()
		self.infos = {
			'name': li.find('h3', {'class': 'a-size-base'}).getText(),
			'author': re.split(r'[,(]', authorInfo[3:len(authorInfo)])[0]
		}

		price = li.find('span', {'class': 'a-offscreen'})
		priority = li.find(string='Prioridade:').find_parent().findAll('span')[1]

		if price: self.infos.update({'price': price.getText()})
		if priority: self.infos.update({'priority': priority.getText()})

		self.infos.update(self.deliveryInfos(li))

		return self.infos

	def deliveryInfos(self, li):
		price = '$0,00'
		delivery = li.find('span', {'class':'wl-item-delivery-badge'})
		if (delivery):
			freeDelivery = delivery.find('a')
			if(freeDelivery):
				prime = True
			else:
				price = re.split(r'[+ \n]', delivery.getText())[2]
				prime = False
				return {'prime': prime, 'delivery': price}
		else:
			prime = False

		return {'prime': prime}

	def	getAllInfos(self):
		allInfo = {
			'moment': datetime.now(),
			'books': []
		}
		try:
			ul = self.listBooks()
			for li in ul:
				allInfo['books'].append(self.getsBookInfo(li))
		except:
			print(TypeError('Undefined Error Occuring: sometimes listBooks() gets soup variable as NoneType. God knows why!'))

		return allInfo
# r2 = s.get('https://images-na.ssl-images-amazon.com/images/I/61-6nKPKyWL.js?AUIClients/AmazonUIjQuery')