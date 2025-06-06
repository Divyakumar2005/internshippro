# from flask import Flask, render_template, request, redirect, url_for
# import mysql.connector
# from datetime import datetime

# app = Flask(__name__)

# # MySQL Database Configuration
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Digidara1000@",
#     database="project"
# )
# cursor = db.cursor()

# # Home page
# @app.route('/')
# def home():
#     return render_template("home.html")

# # Login page
# @app.route('/login')
# def login():
#     return render_template("login.html")

# # Department selection page
# @app.route('/departmentmod')
# def departmentmod():
#     return render_template("departmentmod.html")

# # View attendance records
# @app.route('/view')
# def view():
#     cursor.execute("SELECT s.id, s.name, s.register_number, s.shift, a.status FROM students s LEFT JOIN attendance a ON s.id = a.student_id ORDER BY s.id")
#     records = cursor.fetchall()
#     return render_template("view.html", records=records)

# # Attendance form
# @app.route('/attendance', methods=['GET', 'POST'])
# def attendance():
#     if request.method == 'POST':
#         data = request.form
#         for key in data:
#             if key.startswith('status_'):
#                 student_id = key.split('_')[1]
#                 status = data[key]
#                 date = datetime.today().strftime('%Y-%m-%d')
#                 cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)", (student_id, date, status))
#         db.commit()
#         return redirect(url_for('success'))
#     else:
#         cursor.execute("SELECT * FROM students")
#         students = cursor.fetchall()
#         return render_template("newmarkattlist.html", students=students)

# # Success message
# @app.route('/success')
# def success():
#     return "<h3>✅ Attendance Submitted Successfully!</h3>"

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Digidara1000@",  # Your password
    database="project"         # Your database
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/departmentmod')
def departmentmod():
    return render_template("departmentmod.html")

@app.route('/view')
def view():
    cursor.execute("""
        SELECT s.id, s.name, s.register_number, s.shift,
               (SELECT status FROM attendance WHERE student_id = s.id ORDER BY date DESC LIMIT 1) AS latest_status
        FROM students s
    """)
    records = cursor.fetchall()
    return render_template("view.html", records=records)

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        data = request.form
        for key in data:
            if key.startswith('status_'):
                student_id = key.split('_')[1]
                status = data[key]
                date = datetime.today().strftime('%Y-%m-%d')
                cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)", (student_id, date, status))
        db.commit()
        return redirect(url_for('success'))
    else:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return render_template("newmarkattlist.html", students=students)

@app.route('/success')
def success():
    return "<h2 style='text-align:center;'>✅ Attendance Submitted Successfully!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
