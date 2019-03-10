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
      js["R1"]["Physical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})

    R1_org=df_R1[df_R1['subsector']=='Organisational']
    for index, row in R1_org.iterrows():
      js["R1"]["Organisational"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})

    R1_tec=df_R1[df_R1['subsector']=='Technical']
    for index, row in R1_tec.iterrows():
      js["R1"]["Technical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})


    R2_phy=df_R2[df_R2['subsector']=='Physical']
    for index, row in R2_phy.iterrows():
      js["R2"]["Physical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})

    R2_org=df_R2[df_R2['subsector']=='Organisational']
    for index, row in R2_org.iterrows():
      js["R2"]["Organisational"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})

    R2_tec=df_R2[df_R2['subsector']=='Technical']
    for index, row in R2_tec.iterrows():
      js["R2"]["Technical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})


    R3_phy=df_R3[df_R3['subsector']=='Physical']
    for index, row in R3_phy.iterrows():
      js["R3"]["Physical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})

    R3_org=df_R3[df_R3['subsector']=='Organisational']
    for index, row in R3_org.iterrows():
      js["R3"]["Organisational"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})

    R3_tec=df_R3[df_R3['subsector']=='Technical']
    for index, row in R3_tec.iterrows():
      js["R3"]["Technical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})


    R4_phy=df_R4[df_R4['subsector']=='Physical']
    for index, row in R4_phy.iterrows():
      js["R4"]["Physical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})

    R4_org=df_R4[df_R4['subsector']=='Organisational']
    for index, row in R4_org.iterrows():
      js["R4"]["Organisational"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})

    R4_tec=df_R4[df_R4['subsector']=='Technical']
    for index, row in R4_tec.iterrows():
      js["R4"]["Technical"].append({'qid':row["qid"], 'question': row["question"], 'cid': row["category_id"],  'cname': row["category_name"]})

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
    dbinstance_usr = 'root'
    dbinstance_pwd = 'root'
    dbinstance_ip       = 'localhost'
    schema     = 'BKBASE'
    db = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(dbinstance_usr, dbinstance_pwd,dbinstance_ip, schema))
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
   uid='%s' % userid
   uid=uid.strip("'")
   query = [{'$match':{'userid':uid}},{'$unwind' : "$rows" }, { '$match' : { "rows.sector" : { '$eq' : sector  } }} ]

   document = col.aggregate(query)
   return document

def getSurveyDetailsByCid(userid,survey,company,host,base,colection,user,pwd,subsector,sector):
   col=mongoConnect(host,base,colection,user,pwd)

   query = [{'$match':{"userid":userid.strip('"')}},{'$unwind' : "$rows" }, { '$match' : { "rows.subsector" : { '$eq' : subsector  }, "rows.sector" : {'$eq' : sector} }} ]
   document = col.aggregate(query)
   return document

def mongoInit(colection):
    host='localhost'
    base='BKBASE'
    colection='users'
    user='root'
    pwd='root'
    return host,base,colection,user,pwd


def getSurveyQuestions(sur,comp,host,base,colection,user,pwd,sector):
   col=mongoConnect(host,base,colection,user,pwd)

   sur='%s' % sur
   sur=sur.strip("'")
   comp='%s' % comp
   comp=comp.strip("'")
   sector='%s' % sector
   sector=sector.strip("'")

   query = [ {'survey':sur,'company':comp},{ sector: 1 }]
 #  print("HII", query)
   document = col.find({'survey':"ITH",'company':"MYSUR"},{ 'R1': 1 })

  # for i in document:
  #     print(i)
   return document
