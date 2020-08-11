from pymongo import MongoClient
from listProducts import *
from dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv(dotenv_path='.env')

# getting site information
url = os.getenv('url')
site = GetSite(url)

# connecting with MongoDB
user = os.getenv('user')
password = os.getenv('password')
cluster = os.getenv('cluster')

conString = 'mongodb+srv://'+user+':'+password+'@'+cluster+'.kivsk.gcp.mongodb.net'
client = MongoClient(conString)
db = client.get_database('amazon')

if url not in db.list_collection_names():
	db.create_collection(url)
col = db.get_collection(url)


allInfo = site.getAllInfos()
if allInfo: col.insert_one(allInfo)