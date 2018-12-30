import pandas as pd
from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client['BKBASE']

a=db.users.find({
    'F649081.userid': 'F649081', 'survey': 'Survey Name', 'company': 'Company Name' }, {'F649081.R1.Physical.cid':1})


for i in a:
    print(i)
