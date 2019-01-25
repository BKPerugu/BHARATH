import json
import smtplib
import sqlalchemy
from pymongo import MongoClient

# access row by row and update the json file
def parseDF(df_R1,df_R2,df_R3,df_R4,jsonFile,survey,company):
    with open(jsonFile) as json_data:
        js = json.load(json_data)

    #updating surveyName and CompanyName
    js["survey"]=survey
    js["company"]=company

    #updating qid, cid & questions to json file

    R1_phy=df_R1[df_R1['subsector']=='Physical']
    for index, row in R1_phy.iterrows():
      js["R1"]["Physical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})

    R1_org=df_R1[df_R1['subsector']=='Organisational']
    for index, row in R1_org.iterrows():
      js["R1"]["Organisational"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})

    R1_tec=df_R1[df_R1['subsector']=='Technical']
    for index, row in R1_tec.iterrows():
      js["R1"]["Technical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})


    R2_phy=df_R2[df_R2['subsector']=='Physical']
    for index, row in R2_phy.iterrows():
      js["R2"]["Physical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})

    R2_org=df_R2[df_R2['subsector']=='Organisational']
    for index, row in R2_org.iterrows():
      js["R2"]["Organisational"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})

    R2_tec=df_R2[df_R2['subsector']=='Technical']
    for index, row in R2_tec.iterrows():
      js["R2"]["Technical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})


    R3_phy=df_R3[df_R3['subsector']=='Physical']
    for index, row in R3_phy.iterrows():
      js["R3"]["Physical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})

    R3_org=df_R3[df_R3['subsector']=='Organisational']
    for index, row in R3_org.iterrows():
      js["R3"]["Organisational"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})

    R3_tec=df_R3[df_R3['subsector']=='Technical']
    for index, row in R3_tec.iterrows():
      js["R3"]["Technical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})


    R4_phy=df_R4[df_R4['subsector']=='Physical']
    for index, row in R4_phy.iterrows():
      js["R4"]["Physical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})

    R4_org=df_R4[df_R4['subsector']=='Organisational']
    for index, row in R4_org.iterrows():
      js["R4"]["Organisational"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})

    R4_tec=df_R4[df_R4['subsector']=='Technical']
    for index, row in R4_tec.iterrows():
      js["R4"]["Technical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"]})

    with open(jsonFile, 'w') as outfile:
      json.dump(js, outfile)



# Establishes connection to MongoDB specified collection
def mongoConnect(host,base,colection,user,pwd):

    client = MongoClient(host, 27017)
    db = client[base]
    col = db[colection]
    return col


# load json to questions collection
def pushMongoDB(host,database,collection,jsonFile,user,pwd,survey,company):

    col = mongoConnect(host,database,collection,user,pwd)
    #check if same survey & comany names alreaday exists in database.. if yes, delte the existing entry in database
    col.remove({"survey":survey,"company":company})

    #inserting the json file as document into datbase
    with open(jsonFile) as f:
      data = json.load(f)
    col.insert(data)


def getTimeStamp():
    import calendar
    import time
    return calendar.timegm(time.gmtime())



def getMails(survey,company,department):
    db=sqlConnect()
   # SELECT email  FROM bkbase.userdetails where survey='BKSurvey' and company='CGI' and department ='adv' and isValid='False' and surveyActive='True'
    result = db.engine.execute("SELECT email  FROM userdetails where survey='"+survey+ "' and company='"+company + "' and department ='"+department+"'")
    return result


def sqlConnect():
    database_username = 'root'
    database_password = 'root'
    database_ip       = 'localhost'
    database_name     = 'BKBASE'
    db = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(database_username, database_password,database_ip, database_name))
    return db

def activateSurvey(survey,company,department):
    db=sqlConnect()
    # SELECT email  FROM bkbase.userdetails where survey='BKSurvey' and company='CGI' and department ='adv' and isValid='False' and surveyActive='True'
    db.engine.execute("UPDATE userdetails set activateSurvey='True' where survey='"+survey+ "' and company='"+company + "' and department ='"+department+"' and activateSurvey='False'")

def pushSurvey(mail_list):
    for mail in mail_list:
        sender = 'root@ith.com'
        receivers = mail

        message = """ 
        
        MAIL BODY ## MAIL BODY ## MAIL BODY  
        Click on the below link to take SURVEY
        
        http://survey.com:5000
                
        """

        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")


def getSurveyDetails(userid,survey,company,host,base,colection,user,pwd,sector):
   col=mongoConnect(host,base,colection,user,pwd)
   query = [{'$match':{"userid":'1234'}},{'$unwind' : "$rows" }, { '$match' : { "rows.sector" : { '$eq' : sector  } }} ]
   document = col.aggregate(query)
   return document

def getSurveyDetailsByCid(userid,survey,company,host,base,colection,user,pwd,subsector,sector):
   col=mongoConnect(host,base,colection,user,pwd)
   query = [{'$match':{"userid":userid}},{'$unwind' : "$rows" }, { '$match' : { "rows.subsector" : { '$eq' : subsector  }, "rows.sector" : {'$eq' : sector} }} ]
   document = col.aggregate(query)
   return document

def mongoInit():
    host='localhost'
    base='BKBASE'
    colection='users'
    user='root'
    pwd='root'
    return host,base,colection,user,pwd




