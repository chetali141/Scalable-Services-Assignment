import json

#Read the JSON Data File
dataFile = open('Data.json')
data = json.load(dataFile)
dataFile.close()

def addNewBook(newtitle, newauthor, newlength):
    newid = len(data) + 1
    addBook = {'id': newid, 'title': newtitle, 'author': newauthor, 'length': newlength}
    data.append(addBook)
    with open('Data.json', "w") as file:
        json.dump(data, file)
    return "Your request has been submitted successfully. The book will be available soon."
