import pandas as pd
import json


with open("C:/Users/bhara/Desktop/workspace/temp/user.json") as datafile:
    data = json.load(datafile)
df = pd.DataFrame(data)

print(df.rows[0])
