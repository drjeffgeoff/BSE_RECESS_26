# Import flask
from flask import Flask, render_template

# Create an Instance of a flask class
# ''__name__" is a special variable that tells Flask where to look for resouces

app = Flask(__name__)

#Decorator: /about : Maps the URL '/' 

@app.route('/')

# Define a function to display text Welcome to Flask

def home():
    # Write the Text that can be displayed on your browser
    return '<h1> Welcome to Flask Framework </h2>'

# Route to about
@app.route('/about')

def about():
    return '<h1> Welcome to  </h2>'

# Dynamic Routing
@app.route('/contact/<name>')

def contact(name):
    return f'Welcome to {name}'


# Profile Create Dynamic Route
@app.route('/user/<string:username>/<int:user_id>')

# Defined the profile function
def profile(username,user_id):
    # Data passed from python to the template
    return render_template('profile.html', username=username, user_id=user_id)

# Template Inheritance (Base Template)

# To Ensure your server runs only if this script is executed directly

if __name__ == '__main__':
    app.run(debug=True)