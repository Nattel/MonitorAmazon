from listProducts import *

url = 'https://www.amazon.com.br/hz/wishlist/ls/Y4THLN39W7GZ#store'

con = listConnection(url)

for li in listBooks(con):
	print(getsBookInfo(li))