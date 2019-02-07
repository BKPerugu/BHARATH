"""

This utility extracts user details from excel and inserts as records in MYSQL `userdetails` table.
columns:
    userid
    username
    email
    department
    company
    password
    isValid
    survey

execution: python usersExtraction.py surveyName companyName

"""

import pandas as pd
import sys
import sqlalchemy


survey = sys.argv[1]
cmp = sys.argv[2]

# Parsing excel data
df = pd.read_excel('C:/Users/bhara/Desktop/workspace/user_details.xlsx')
print(df)
#Parsing data from excel
df=df.sort_values(by ='username', ascending=True)
df['company']=cmp
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


