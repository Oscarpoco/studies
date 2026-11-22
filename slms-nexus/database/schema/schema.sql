-- SLMS_Nexus schema (SQLite3)
-- Foreign keys enforce valid EmployeeID and LeaveTypeID on LeaveApplications

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS LeaveApplications;
DROP TABLE IF EXISTS LeaveTypes;
DROP TABLE IF EXISTS Employees;

CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Department VARCHAR(80) NOT NULL,
    JobTitle VARCHAR(80),
    DateJoined DATE NOT NULL,
    AnnualLeaveBalance INTEGER DEFAULT 20
);

CREATE TABLE LeaveTypes (
    LeaveTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    TypeName VARCHAR(50) NOT NULL,
    MaxDaysAllowed INTEGER NOT NULL
);

CREATE TABLE LeaveApplications (
    ApplicationID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeID INTEGER NOT NULL,
    LeaveTypeID INTEGER NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    NumberOfDays INTEGER NOT NULL,
    Reason TEXT,
    Status VARCHAR(20) DEFAULT 'Pending'
        CHECK (Status IN ('Pending', 'Approved', 'Rejected', 'Cancelled')),
    ApprovedBy VARCHAR(100),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (LeaveTypeID) REFERENCES LeaveTypes(LeaveTypeID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
