from flask import Flask

# Setup the app
app = Flask(__name__)

# Create a index route for browing the URL
@app.route('/')
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)