from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name/<user>')
def name(user):
    return f"<h1>Hello {user}!!</h1>"



#Create error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_not_found(e):
    return render_template('500.html'), 500
