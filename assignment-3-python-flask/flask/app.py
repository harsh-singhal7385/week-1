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
    
    if request.method == "POST":
        title_data = request.form['title']
        description_data = request.form['description']
        todo = ToDoList(title = title_data, description = description_data)
        db.session.add(todo)
        db.session.commit()
    all_to_do = ToDoList.query.all()
    
    return render_template('./index.html',allTodo = all_to_do)


@app.route('/update/<int:index>', methods = ['GET', 'POST'])
def update_data(index):
    if request.method == "POST":
        title_data = request.form['title']
        description_data = request.form['description']
        todo = ToDoList.query.filter_by(index = index).first()
        todo.title = title_data
        todo.description = description_data
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    all_todo = ToDoList.query.filter_by(index = index).first()
    
    return render_template('./update.html',allTodo = all_todo)


@app.route('/delete/<int:index>', methods = ['GET', 'POST'])
def delete_data(index):
    all_todo = ToDoList.query.filter_by(index = index).first()
    db.session.delete(all_todo)
    db.session.commit()
    return redirect('/')


@app.route('/search', methods = ['GET', 'POST'])
def search_data(index):
    all_todo = ToDoList.query.filter_by(index = index).first()
    return redirect('/')


@app.route('/getlist', methods = ['GET', 'POST'])
def get_list_data():
    return redirect('/')


if __name__== '__main__':
    app.run(debug=True) 