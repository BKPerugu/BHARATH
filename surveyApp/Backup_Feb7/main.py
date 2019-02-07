from flask import Flask, request, render_template
import businessLogic as bl
import os
import pandas as pd
import chartsLogic as cl
import numpy as np
import functools as ft

sectors=['R1','R2','R3','R4']
subsectors=['Physical','Organisational','Technical']
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def login():
    return "<u><b>Login Page</u></b>"
## Redirect to login page


@app.route('/questionsUpload', methods=['GET', 'POST'])
def questionsUpload():
    survey = request.args.get('survey')
    company = request.args.get('company')
    command = 'python C:/Users/bhara/PycharmProjects/Survey/questionsExtraction.py ' + company+ ' ' +survey
    os.system(command)
    os.system('python C:/Users/bhara/PycharmProjects/Survey/questionsExtractions.py {} {}'.format(company,survey))
    return 'Upload Done -- replace this with web page'


@app.route('/usersUpload', methods=['GET', 'POST'])
def usersUpload():
    survey = request.args.get('survey')
    company = request.args.get('company')

    command = 'python C:/Users/bhara/PycharmProjects/Survey/usersExtraction.py ' + company+ ' ' +survey
    os.system(command)
    return 'Upload Done -- replace this with web page'


@app.route('/releaseSurvey', methods=['GET', 'POST'])
def releaseSurvey():
    survey = request.args.get('survey')
    company = request.args.get('company')
    department = request.args.get('department')
    bl.activateSurvey(survey,company,department)
    mail_list=list(bl.getMails(survey,company,department))
    bl.pushSurvey(mail_list)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    folder_name = request.form['superhero']
    '''
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print("folder exist")
    '''
    target = os.path.join(APP_ROOT, 'files/{}'.format(folder_name))
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        # This is to verify files are supported

        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete.html", image_name=filename)


@app.route('/chartsOne', methods=['GET', 'POST'])
def chartsOne():

    survey = request.args.get('survey')
    company = request.args.get('company')
    userid= request.args.get('userid')
    host,base,colection,dbuser,pwd=bl.mongoInit()


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

    print(df)
    return 'Done'





if __name__ == '__main__':
    app.run(debug=True)
