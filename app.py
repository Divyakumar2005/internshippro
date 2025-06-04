from flask import Flask, render_template, request, redirect, url_for,session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session handling

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'your_database_name'
}

# ---------- ROUTES ----------

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return "Invalid credentials", 401

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('home.html', username=session['username'])

@app.route('/department')
def department():
    return render_template('department.html')

@app.route('/newentry')
def new_entry():
    return render_template('new(newentry).html')

@app.route('/shift')
def shift():
    return render_template('shift.html')

@app.route('/view')
def view():
    return render_template('view.html.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# ---------- MAIN ----------
if __name__ == '__main__':
    app.run(debug=True)
