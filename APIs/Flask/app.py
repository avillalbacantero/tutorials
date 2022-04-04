from flask import Flask, render_template

# Setup the app
app = Flask(__name__)

# Create a index route for browing the URL
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)