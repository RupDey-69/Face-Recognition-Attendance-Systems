USE attendance_system;
SELECT * FROM attendance_system.Attendence;

CREATE TABLE Attendence (

id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
mobile VARCHAR(15),
email VARCHAR(100),
roll VARCHAR(20),
father VARCHAR(100),
mother VARCHAR(100),
course VARCHAR(50),
dob DATE,
address TEXT

);



