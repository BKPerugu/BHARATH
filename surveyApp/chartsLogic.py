import matplotlib.pyplot as plt
import mpld3 as mp
import businessLogic as bl
import pandas as pd
import json


def calculate(R_df):

  phy=R_df[R_df['subsector']=='Physical']
  org=R_df[R_df['subsector']=='Organisational']
  tech=R_df[R_df['subsector']=='Technical']
  phycid=phy.cid.unique()
  orgcid=org.cid.unique()
  techcid=tech.cid.unique()

  subs=['Physical','Organisational','Technical']
  host,base,colection,user,pwd=bl.mongoInit()
  ## userid,survey,company  should be passed from UI with API
  ##userid='588'
  ##company='ITH'
  ##survey='Quater 1'

  x=df=pd.DataFrame()
  for sub in subs:
    subdf=R_df[R_df['subsector']==sub]
    subcid=subdf.cid.unique()

    for i in subcid:
        print("i value is ", i, sub)
        subscore=subdf[subdf.cid==i].qscore.sum()/len(subdf[subdf.cid==i].index)
        df=subdf[subdf.cid==i]
        df['cscore']=subscore
        x=pd.concat([df, x], ignore_index=True)
        print(subcid)

  df=x.sort_values(['cid']) # df has mean values of cscore i.e category score in R1
  print(df)
  return df


def pie(df):

    pieR1=df[df['sector']=='R1']['avgsectscore'].unique()
    pieR1= round(float(pieR1),2)

    pieR2=df[df['sector']=='R2']['avgsectscore'].unique()
    pieR2= round(float(pieR2),2)

    pieR3=df[df['sector']=='R3']['avgsectscore'].unique()
    pieR3= round(float(pieR3),2)

    pieR4=df[df['sector']=='R4']['avgsectscore'].unique()
    pieR4= round(float(pieR4),2)

    data = json.dumps({'R1': pieR1, 'R2': pieR2, 'R3':pieR3, 'R4':pieR4})
    return data


def bar(df):

    barR1=[]
    barR1.append(round(float(df[(df['sector']=='R1') & (df['subsector']=='Physical')]['subsector_avg'].unique()),2))
    barR1.append(round(float(df[(df['sector']=='R1') & (df['subsector']=='Organisational')]['subsector_avg'].unique()),2))
    barR1.append(round(float(df[(df['sector']=='R1') & (df['subsector']=='Technical')]['subsector_avg'].unique()),2))

    barR2=[]
    barR2.append(round(float(df[(df['sector']=='R2') & (df['subsector']=='Physical')]['subsector_avg'].unique()),2))
    barR2.append(round(float(df[(df['sector']=='R2') & (df['subsector']=='Organisational')]['subsector_avg'].unique()),2))
    barR2.append(round(float(df[(df['sector']=='R2') & (df['subsector']=='Technical')]['subsector_avg'].unique()),2))

    barR3=[]
    barR3.append(round(float(df[(df['sector']=='R3') & (df['subsector']=='Physical')]['subsector_avg'].unique()),2))
    barR3.append(round(float(df[(df['sector']=='R3') & (df['subsector']=='Organisational')]['subsector_avg'].unique()),2))
    barR3.append(round(float(df[(df['sector']=='R3') & (df['subsector']=='Technical')]['subsector_avg'].unique()),2))

    barR4=[]
    barR4.append(round(float(df[(df['sector']=='R4') & (df['subsector']=='Physical')]['subsector_avg'].unique()),2))
    barR4.append(round(float(df[(df['sector']=='R4') & (df['subsector']=='Organisational')]['subsector_avg'].unique()),2))
    barR4.append(round(float(df[(df['sector']=='R4') & (df['subsector']=='Technical')]['subsector_avg'].unique()),2))

    data = json.dumps({'R1': barR1, 'R2': barR2, 'R3':barR3, 'R4':barR4})
    return data

