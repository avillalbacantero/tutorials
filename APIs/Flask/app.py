from crypt import methods
from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Setup the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
db = SQLAlchemy(app)  # initialize the DB

#db.create_all()  # create DB

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<Task {self.id}>"

# Create a index route for browing the URL
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        task_content = request.form["content"]
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            raise e
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        raise e("There was a problem deleting that task")
    
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    
    task = Todo.query.get_or_404(id)
    
    if request.method == "POST":
        task.content = request.form["content"]
        
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            raise e("Couldn't update task.")
    else:
        return render_template("update.html", task=task)

if __name__ == "__main__":
    app.run(debug=True)