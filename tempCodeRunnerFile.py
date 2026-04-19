from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
app.app_context().push()
class Todo(db.Model):
    Sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f"{self.Sno} - {self.title}"


    

@app.route('/')
def hello_world():
    todo=Todo(title="First todo",desc="Start investing in Stocks market")
    db.session.add(todo)
    db.session.commit()
    allTodo=Todo.query.all()
    print(allTodo)
    return render_template('index.html',allTodo=allTodo)
    # return 'Hello, World!'

@app.route('/products')
def products():
    allTodo=Todo.query.all()
    print(allTodo)
    return 'This is products page'

if __name__ == '__main__':
    app.run(debug=True, port=8000)