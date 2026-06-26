from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# DATABASE CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rupdey@#2006",
    database="attendance_system"
)

cursor = db.cursor()

if db.is_connected():
    print(" Database Connected Successfully")

# HOME
@app.route('/')
def home():
    return render_template('index.html')


# LOGIN
@app.route('/login')
def login_page():
    return render_template('login.html')


# REGISTER PAGE
@app.route('/register')
def register():
    return render_template('register.html')


# REGISTER STUDENT (POST)
@app.route('/register_student', methods=['POST'])
def register_student():

    Name = request.form['name']
    Mobile_Number = request.form['mobile']
    Email = request.form['email']
    Roll = request.form['roll']
    Father = request.form['father']
    Mother = request.form['mother']
    Course = request.form['course']

    Dob = request.form.get('dob')
    if Dob == "":
        Dob = None

    Address = request.form['address']

    sql = """
    INSERT INTO Attendance
    (name,mobile_number,email,roll,father,mother,course,dob,address)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        Name,
        Mobile_Number,
        Email,
        Roll,
        Father,
        Mother,
        Course,
        Dob,
        Address
    )

    cursor.execute(sql, values)
    db.commit()

    return redirect('/students')


# VIEW STUDENTS
@app.route('/students')
def students():
    cursor.execute("SELECT * FROM Attendance")
    data = cursor.fetchall()
    return render_template("students.html", students=data)


# CAMERA
@app.route('/configure_camera')
def configure_camera():
    return render_template('configure_camera.html')


# ADMIN
@app.route('/admin')
def admin():
    return render_template('admin.html')


# MARK ATTENDANCE (ADD THIS)
@app.route('/mark_attendance')
def mark_attendance():
    return render_template('mark_attendance.html')


# VIEW ATTENDANCE (ADD THIS)
@app.route('/view_attendance')
def view_attendance():
    return render_template('view_attendance.html')


# REPORTS (ADD THIS)
@app.route('/reports')
def reports():
    return render_template('reports.html')


if __name__ == "__main__":
    app.run(debug=True)
    
