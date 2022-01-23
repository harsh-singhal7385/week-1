from datetime import datetime
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydatabase.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ToDoList(db.Model):
    index = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(400), nullable = False)
    datetime_var = db.Column(db.DateTime, default = datetime.utcnow)


@app.route('/', methods = ['GET', 'POST'])
def home_page():
    
    if request.method == "GET":
        titleData = request.form['title']
        descriptionData = request.form['description']
        todo = ToDoList(title = titleData, description = descriptionData)
        db.session.add(todo)
        db.session.commit()
        allTodo = ToDoList.query.all()
    
    return render_template('./index.html',allTodo = "")


@app.route('/add', methods = ['GET', 'POST'])
def addData():
    if request.method == "POST":
        titleData = request.form['title']
        descriptionData = request.form['description']
        todo = ToDoList(title = titleData, description = descriptionData)
        db.session.add(todo)
        db.session.commit()
        allTodo = ToDoList.query.all()
    
        return redirect('/',)


@app.route('/update', methods = ['GET', 'POST'])
def updateData():
    return redirect('/')


@app.route('/delete', methods = ['GET', 'POST'])
def deleteData():
    return redirect('/')


@app.route('/search', methods = ['GET', 'POST'])
def searchData():
    return redirect('/')


@app.route('/getlist', methods = ['GET', 'POST'])
def getlistData():
    return redirect('/')


if __name__== '__main__':
    app.run(debug=True) 