from listProducts import *
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')
url = os.getenv('url')
con = listConnection(url)

for li in listBooks(con):
	print(getsBookInfo(li))