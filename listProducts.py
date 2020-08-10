import requests
from bs4 import BeautifulSoup
import re

def listConnection(url):
	s = requests.session()
	r = s.get(url)

	return BeautifulSoup(r.text, 'html.parser')

def listBooks(soup):
	# aims first for the 'center' div where the books are and then enlists them
	divs = soup.find('div', {'id': 'content-right'}).find('div', {'id': 'item-page-wrapper'})
	lis = divs.find('ul').findAll('li')

	return lis


def getsBookInfo(li):
	authorInfo = li.find('span', {'class': 'a-size-base'}).getText()
	infos = {
		'name': li.find('h3', {'class': 'a-size-base'}).getText(),
		'author': re.split(r'[,(]', authorInfo[3:len(authorInfo)])[0]
	}

	price = li.find('span', {'class': 'a-offscreen'})
	priority = li.find(string='Prioridade:').find_parent().findAll('span')[1]

	if price: infos.update({'price': price.getText()})
	if priority: infos.update({'priority': priority.getText()})

	infos.update(deliveryInfos(li))

	return infos

def deliveryInfos(li):
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

# r2 = s.get('https://images-na.ssl-images-amazon.com/images/I/61-6nKPKyWL.js?AUIClients/AmazonUIjQuery')