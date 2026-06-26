USE attendance_system;
SELECT * FROM Attendance;


CREATE TABLE Attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    mobile_number VARCHAR(15),
    email VARCHAR(100),
    roll VARCHAR(20),
    father VARCHAR(100),
    mother VARCHAR(100),
    course VARCHAR(50),
    dob DATE,
    address TEXT
);

