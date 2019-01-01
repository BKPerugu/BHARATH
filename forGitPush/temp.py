import pandas as pd
from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client['BKBASE']


con= [{"$match":{"userid":'J649081'}},{"$unwind" : "$rows"}, {"$match" : {"rows.cid" : {"$eq" : 3} }}]
a=db.users.aggregate(con)

for i in a:
    print(i)
    print(i['rows']['cid'])
