import pandas as pd
import json

#Read the JSON Data File
dataFile = open('Data.json')
data = json.load(dataFile)
dataFile.close()

def fetchBooks():
    columns = ['id','title','author','length']
    df = pd.DataFrame(data, columns=columns)
    table = df.to_html(index=False)
    return table

