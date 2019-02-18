from flask import Flask, request, render_template
import requests
import businessLogic as bl
import os
import pandas as pd
from shutil import copyfile
import chartsLogic as cl
import json
import numpy as np
import functools as ft
from flask_jsonpify import jsonify
import pprint
import sqlalchemy


sectors=['R1','R2','R3','R4']
subsectors=['Physical','Organisational','Technical']
df=pd.DataFrame()
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))



@app.route('/')
def login():
    return "<u><b>Login Page</u></b>"
## Redirect to login page


@app.route('/questionsUpload', methods=['GET','POST'])
def questionsUpload():
    survey = request.args.get('survey')
    company = request.args.get('company')
    file = request.files['file']
    df = pd.read_excel(file)

    #Getting timestamp
    backup=bl.getTimeStamp()
    
    #code pending for taking backup of this json
    jFile= 'C:/Users/bhara/Desktop/workspace/db.json'
    jsonFile= 'C:/Users/bhara/Desktop/workspace/db_{}.json'.format(backup)
    copyfile(jFile, jsonFile)

    #Parsing and divding into sector chunks of data from excel
    df_R1 = df[df['sector']=='R1']
    df_R2 = df[df['sector']=='R2']
    df_R3 = df[df['sector']=='R3']
    df_R4 = df[df['sector']=='R4']
    
    #initialize Mongo DB details or can be taken from a config file in future
    host='localhost'
    database='BKBASE'
    collection='questions'
    user='root'
    pwd='Blackpearl'
    
    
    #update the db.json file with related info
    bl.parseDF(df_R1,df_R2,df_R3,df_R4,jsonFile,survey,company)
    
    #push json to mongo
    bl.pushMongoDB(host,database,collection,jsonFile,user,pwd,survey,company)
    
    #function to clean the workspace and close all handlers and files
    #bl.cleanup()
    
    return 'Upload Done -- replace this with web page'


@app.route('/usersUpload', methods=['GET','POST'])
def usersUpload():
    survey = request.args.get('survey')
    company = request.args.get('company')
    file = request.files['file']
    df = pd.read_excel(file)

    #Parsing data from excel
    df=df.sort_values(by ='username', ascending=True)
    df['company']=company
    df['survey']=survey
    df['password']='default123'
    df['isValid']='False'
    df['activateSurvey']='False'
    df.set_index('username',inplace=True)

    database_username = 'root'
    database_password = 'root'
    database_ip       = 'localhost'
    database_name     = 'BKBASE'
    database_connection = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(database_username, database_password,database_ip, database_name))


    # write the DataFrame to a table in the sql database
    df.to_sql(con=database_connection, name='userdetails', if_exists='append')



    #command = 'python C:/Users/bhara/PycharmProjects/Survey/usersExtraction.py ' + company+ ' ' +survey +' ' +filename
    #os.system(command)
    return 'Upload Done -- replace this with web page'


@app.route('/releaseSurvey', methods=['GET'])
def releaseSurvey():
    survey = request.args.get('survey')
    company = request.args.get('company')
    department = request.args.get('department')
    bl.activateSurvey(survey,company,department)
    mail_list=list(bl.getMails(survey,company,department))
    bl.pushSurvey(mail_list)


@app.route('/chartsOne', methods=['GET'])
def chartsOne():

    survey = request.args.get('survey')
    company = request.args.get('company')
    userid= request.args.get('userid')
    host,base,colection,dbuser,pwd=bl.mongoInit('users')


    df=pd.DataFrame(columns=['sector','subsector','cid','qid','qscore','qconfidence'])
    for sector in sectors:
        document= bl.getSurveyDetails(userid,survey,company,host,base,colection,dbuser,pwd,sector)
        for i in document:
            df=df.append({'sector': i['rows']['sector'],'subsector':i['rows']['subsector'],'cid':i['rows']['cid'],'qid':i['rows']['qid'],'qscore':i['rows']['qscore'], 'qconfidence':i['rows']['qconfidence']},ignore_index=True)
    df=df.sort_values(['sector','subsector'])

    R1_df=df[df['sector']=='R1']
    R2_df=df[df['sector']=='R2']
    R3_df=df[df['sector']=='R3']
    R4_df=df[df['sector']=='R4']

    R1_df=cl.calculate(R1_df)
    R2_df=cl.calculate(R2_df)
    R3_df=cl.calculate(R3_df)
    R4_df=cl.calculate(R4_df)

    framelist=[R1_df,R2_df,R3_df,R4_df]
    mf=pd.DataFrame(columns=R1_df.columns.values)
    for i in framelist:
        phy=i[i['subsector']=='Physical']
        org=i[i['subsector']=='Organisational']
        tech=i[i['subsector']=='Technical']

        i['avgsectscore']=(phy.iloc[0]['cscore']+org.iloc[0]['cscore']+tech.iloc[0]['cscore'])/3
        mf=mf.append(i)
        mf.index = pd.RangeIndex(len(mf.index))

        avgR1_phy=mf[(mf['subsector']=='Physical') & (mf['sector']=='R1')].qscore.sum()/len(mf[(mf['subsector']=='Physical') & (mf['sector']=='R1')])

    avgR1_phy=mf[(mf['subsector']=='Physical') & (mf['sector']=='R1')].qscore.sum()/len(mf[(mf['subsector']=='Physical') & (mf['sector']=='R1')])
    avgR1_org=mf[(mf['subsector']=='Organisational') & (mf['sector']=='R1')].qscore.sum()/len(mf[(mf['subsector']=='Organisational') & (mf['sector']=='R1')])
    avgR1_tech=mf[(mf['subsector']=='Technical') & (mf['sector']=='R1')].qscore.sum()/len(mf[(mf['subsector']=='Technical') & (mf['sector']=='R1')])

    avgR2_phy=mf[(mf['subsector']=='Physical') & (mf['sector']=='R2')].qscore.sum()/len(mf[(mf['subsector']=='Physical') & (mf['sector']=='R2')])
    avgR2_org=mf[(mf['subsector']=='Organisational') & (mf['sector']=='R2')].qscore.sum()/len(mf[(mf['subsector']=='Organisational') & (mf['sector']=='R2')])
    avgR2_tech=mf[(mf['subsector']=='Technical') & (mf['sector']=='R2')].qscore.sum()/len(mf[(mf['subsector']=='Technical') & (mf['sector']=='R2')])

    avgR3_phy=mf[(mf['subsector']=='Physical') & (mf['sector']=='R3')].qscore.sum()/len(mf[(mf['subsector']=='Physical') & (mf['sector']=='R3')])
    avgR3_org=mf[(mf['subsector']=='Organisational') & (mf['sector']=='R3')].qscore.sum()/len(mf[(mf['subsector']=='Organisational') & (mf['sector']=='R3')])
    avgR3_tech=mf[(mf['subsector']=='Technical') & (mf['sector']=='R3')].qscore.sum()/len(mf[(mf['subsector']=='Technical') & (mf['sector']=='R3')])

    avgR4_phy=mf[(mf['subsector']=='Physical') & (mf['sector']=='R4')].qscore.sum()/len(mf[(mf['subsector']=='Physical') & (mf['sector']=='R4')])
    avgR4_org=mf[(mf['subsector']=='Organisational') & (mf['sector']=='R4')].qscore.sum()/len(mf[(mf['subsector']=='Organisational') & (mf['sector']=='R4')])
    avgR4_tech=mf[(mf['subsector']=='Technical') & (mf['sector']=='R4')].qscore.sum()/len(mf[(mf['subsector']=='Technical') & (mf['sector']=='R4')])



   # mf[(mf['subsector']=='Physical') & (mf['sector']=='R1')]['subsector_avg']=avgR1_phy
   ## mf['subsector_avg'] = np.where(  (mf['subsector']=='Physical') & (mf['sector']=='R1'))

    filter1 = mf[(mf['subsector']=='Physical') & (mf['sector']=='R1')]
    filter1['subsector_avg']=avgR1_phy

    filter2 = mf[(mf['subsector']=='Organisational') & (mf['sector']=='R1')]
    filter2['subsector_avg']=avgR1_org

    filter3 = mf[(mf['subsector']=='Technical') & (mf['sector']=='R1')]
    filter3['subsector_avg']=avgR1_tech

    filter4 = mf[(mf['subsector']=='Physical') & (mf['sector']=='R2')]
    filter4['subsector_avg']=avgR2_phy

    filter5 = mf[(mf['subsector']=='Organisational') & (mf['sector']=='R2')]
    filter5['subsector_avg']=avgR2_org

    filter6 = mf[(mf['subsector']=='Technical') & (mf['sector']=='R2')]
    filter6['subsector_avg']=avgR2_tech

    filter7 = mf[(mf['subsector']=='Physical') & (mf['sector']=='R3')]
    filter7['subsector_avg']=avgR3_phy

    filter8 = mf[(mf['subsector']=='Organisational') & (mf['sector']=='R3')]
    filter8['subsector_avg']=avgR3_org

    filter9 = mf[(mf['subsector']=='Technical') & (mf['sector']=='R3')]
    filter9['subsector_avg']=avgR3_tech

    filter10 = mf[(mf['subsector']=='Physical') & (mf['sector']=='R4')]
    filter10['subsector_avg']=avgR4_phy

    filter11 = mf[(mf['subsector']=='Organisational') & (mf['sector']=='R4')]
    filter11['subsector_avg']=avgR4_org

    filter12 = mf[(mf['subsector']=='Technical') & (mf['sector']=='R4')]
    filter12['subsector_avg']=avgR4_tech

    dfs=[filter1,filter2,filter3,filter4,filter5,filter6,filter7,filter8,filter9,filter10,filter11,filter12]
    df=pd.concat(dfs)

    js=df.to_json()
#    print(df)
    return js





@app.route('/getSinglePie', methods=['GET'])
def getSinglePie():

    survey = request.args.get('survey')
    company = request.args.get('company')
    userid= request.args.get('userid')
    #r = requests.get("http://127.0.0.1:5000/chartsOne?survey='Quarter%201'&company='ITH'&userid='588'")
    r = requests.get("http://127.0.0.1:5000/chartsOne?survey={}&company={}&userid={}".format(survey,company,userid))
    jsonres=r.json()
    df=pd.DataFrame(jsonres)

    data=cl.pie(df)
    return data


@app.route('/getSingleBar', methods=['GET'])
def getSingleBar():

    survey = request.args.get('survey')
    company = request.args.get('company')
    userid= request.args.get('userid')

    r = requests.get("http://127.0.0.1:5000/chartsOne?survey={}&company={}&userid={}".format(survey,company,userid))
    jsonres=r.json()
    df=pd.DataFrame(jsonres)

    data=cl.bar(df)
    return data



@app.route('/getQuestions', methods=['GET'])
def getQuestions():
    survey = request.args.get('survey')
    company = request.args.get('company')
    sector = request.args.get('sector')
    host,base,colection,dbuser,pwd=bl.mongoInit('questions')


    data=bl.getSurveyQuestions(survey,company,host,base,colection,dbuser,pwd,sector)



@app.route('/temp', methods=['GET', 'POST'])
def temp():
   file = request.files['file']
   df = pd.read_excel(file)
   print(df)
   return 'done'



if __name__ == '__main__':
    app.run(debug=True)
