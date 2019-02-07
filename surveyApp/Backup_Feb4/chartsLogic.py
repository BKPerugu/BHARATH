import matplotlib.pyplot as plt
import mpld3 as mp
import businessLogic as bl
import pandas as pd


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

  #df=x.sort_values(['cid']) # df has mean values of cscore i.e category score in R1
  print(df)
  return df

  """document=bl.getSurveyDetailsByCid(userid,survey,company,host,base,colection,user,pwd,subsector='Physical',sector='R1')
  for i in document:
      print(i)"""

  """
  phycid=len(list(R_df[R_df['subsector']=='Physical'].cid.unique()))
  orgcid=len(list(R_df[R_df['subsector']=='Physical'].cid.unique()))
  techcid=len(list(R_df[R_df['subsector']=='Physical'].cid.unique()))
  """
