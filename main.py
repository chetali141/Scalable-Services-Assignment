from flask import *
import listBook, addBook, findBook

app = Flask(__name__, template_folder='template')


@app.route('/')
def hello_world():
   return 'Hello, Welcome to the BookShop!'


@app.route('/getBook', methods=['GET'])
def getBooks():
    bookName = request.args.get('bookName')
    return findBook.find(bookName)


@app.route('/listBooks')  
def listAllBooks():      
    return render_template("list.html",table=listBook.fetchBooks())


@app.route('/requestBook', methods=['POST'])
def requestBook():
    newtitle = request.form['bookName']
    newauthor = request.form['authorName']
    newlength = request.form['length']
    return addBook.addNewBook(newtitle, newauthor, newlength)


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)

