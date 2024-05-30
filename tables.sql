use cozy;

CREATE TABLE Guests (
    Guest_id INT PRIMARY KEY,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Email VARCHAR(100),
    Phone_no INT,
    Address VARCHAR(30),
    DOB DATE
);

CREATE TABLE Rooms (
    Room_id INT PRIMARY KEY,
    Room_number VARCHAR(50),
    Room_type VARCHAR(50),
    Capacity INT,
    Price FLOAT,
    Status VARCHAR(50)
);

CREATE TABLE Bookings (
    Booking_id INT PRIMARY KEY,
    Guest_id INT,
    Room_id INT,
    Check_in_date DATE,
    Check_out_date DATE,
    Booking_date TIMESTAMP,
    Amount DOUBLE,
    Payment_status VARCHAR(20),
    FOREIGN KEY (Guest_id) REFERENCES Guests(Guest_id),
    FOREIGN KEY (Room_id) REFERENCES Rooms(Room_id)
);

CREATE TABLE Payment (
    Payment_id INT PRIMARY KEY,
    Booking_id INT,
    Amount DECIMAL,
    Payment_date TIMESTAMP,
    Payment_method VARCHAR(50),
    FOREIGN KEY (Booking_id) REFERENCES Bookings(Booking_id)
);

CREATE TABLE Staff (
    Staff_id INT PRIMARY KEY,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Email VARCHAR(100),
    Phone_no INT,
    Salary DOUBLE
);

CREATE TABLE Facilities (
    Facility_name VARCHAR(20) PRIMARY KEY,
    Description TEXT
);

CREATE TABLE Reviews (
    Review_id INT PRIMARY KEY,
    Guest_id INT,
    Booking_id INT,
    Rating INT,
    FOREIGN KEY (Guest_id) REFERENCES Guests(Guest_id),
    FOREIGN KEY (Booking_id) REFERENCES Bookings(Booking_id)
);
