from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # or 'login.html' if index is blank

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/department')
def department():
    return render_template('department.html')

@app.route('/memo')
def memo():
    return render_template('memo.html')

@app.route('/new-entry')
def new_entry():
    return render_template('new(newentry).html')

@app.route('/mark-attendance')
def mark_attendance():
    return render_template('newmarkattlist.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/shift')
def shift():
    return render_template('shift.html')

@app.route('/view')
def view():
    return render_template('view.html.html')  # rename the file to view.html ideally

if __name__ == '__main__':
    app.run(debug=True)
