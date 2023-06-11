import json

#Read the JSON Data File
dataFile = open('Data.json')
data = json.load(dataFile)
dataFile.close()

def find(bookName):
    i=0
    while i < len(data):
        if bookName == data[i]['title']:
            return 'Book is available at the library.'
        i = i + 1
    else:
        return 'Book is not available.'

