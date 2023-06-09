from flask import *
import json
import pandas as pd

app = Flask(__name__, template_folder='template')

#Read the JSON Data File
dataFile = open('Data.json')
data = json.load(dataFile)
dataFile.close()


@app.route('/')
def hello_world():
   return 'Hello, Welcome to the BookShop!'


@app.route('/getBook', methods=['GET'])
def getBooks():
    bookName = request.args.get('bookName')
    if bookName in data:
        return 'Book is available at the library.'
    else:
        return 'Book is not available.'


@app.route('/listBooks')  
def listAllBooks():  
    #   context = {'d': data}
    #   return render_template('list.html', books=context)  
    columns = ['id','title','author','length']
    df = pd.DataFrame(data, columns=columns)
    table = df.to_html(index=False)
    
    return render_template("list.html",table=table)


@app.route('/requestBook', methods=['POST'])
def requestBook():
    newtitle = request.form['bookName']
    newauthor = request.form['authorName']
    newlength = request.form['length']
    newid = len(data) + 1
    addBook = {'id': newid, 'title': newtitle, 'author': newauthor, 'length': newlength}
    data.append(addBook)
    with open('Data.json', "w") as file:
        json.dump(data, file)
    return 'Your request has been submitted.'


if __name__ == '__main__':
   app.run()

