from crypt import methods
from datetime import datetime

from flask import Flask, render_template
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
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)