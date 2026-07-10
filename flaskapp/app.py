# app.py
from flask import Flask

# Create an instance of the Flask class.
# '__name__' is a special variable that tells Flask where to look for resources.
app = Flask(__name__)

# Decorator: Maps the URL '/' to the function below.
@app.route('/')
@app.route("/student/<name>")
def student(name):
    return f"Welcome {name}"

if __name__ == "__main__":
    app.run(debug=True)
# Ensures the server runs only if this script is executed directly.
if __name__ == '__main__':
    app.run(debug=True)