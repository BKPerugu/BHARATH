from flask import Flask, request, render_template
import businessLogic as bl
import os
import pandas as pd
import chartsLogic as cl

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
    print(survey+" "+company)
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
    host,base,colection,user,pwd=bl.mongoInit()

    sectors=['R1','R2','R3','R4']
    df=pd.DataFrame(columns=['sector','subsector','cid','qid','qscore','qconfidence'])
    for sector in sectors:
        document= bl.getSurveyDetails(userid,survey,company,host,base,colection,user,pwd,sector)
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


    print(mf)
    return 'Done'



if __name__ == '__main__':
    app.run(debug=True)
