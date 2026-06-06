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

print("Database Connected")


# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# LOGIN PAGE 
@app.route('/login')
def login_page():
    return render_template('login.html')


# REGISTER PAGE
@app.route('/register')
def register():
    return render_template('register.html')



# REGISTER STUDENT
@app.route('/register_student', methods=['POST'])
def register_student():

    name = request.form['name']
    mobile = request.form['mobile']
    email = request.form['email']
    roll = request.form['roll']
    father = request.form['father']
    mother = request.form['mother']
    course = request.form['course']
    dob = request.form['dob']
    address = request.form['address']

    sql = """
    INSERT INTO Attendence
    (name,mobile,email,roll,father,mother,course,dob,address)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (name, mobile, email, roll, father, mother, course, dob, address)

    cursor.execute(sql, values)
    db.commit()

    return redirect('/')


# VIEW STUDENTS
@app.route('/students')
def students():

    cursor.execute("SELECT * FROM Attendence")
    data = cursor.fetchall()

    return render_template("students.html", students=data)


if __name__ == "__main__":
    app.run(debug=True)
