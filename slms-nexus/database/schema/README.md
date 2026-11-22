# schema.sql — line by line

Builds the three SLMS tables and rules in SQLite.

| Line | Code | What it does |
|------|------|--------------|
| 1–2 | Comments | File purpose. |
| 4 | `PRAGMA foreign_keys = ON` | Turn on FK checks for this connection. |
| 6 | `DROP TABLE IF EXISTS LeaveApplications` | Remove old apps table first (depends on others). |
| 7 | `DROP TABLE IF EXISTS LeaveTypes` | Remove leave types if present. |
| 8 | `DROP TABLE IF EXISTS Employees` | Remove employees if present. |
| 10 | `CREATE TABLE Employees (` | Start Employees table. |
| 11 | `EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT` | Unique ID; SQLite fills next number. |
| 12 | `FirstName VARCHAR(50) NOT NULL` | Required first name. |
| 13 | `LastName VARCHAR(50) NOT NULL` | Required last name. |
| 14 | `Email VARCHAR(100) NOT NULL UNIQUE` | Required; no two staff share email. |
| 15 | `Department VARCHAR(80) NOT NULL` | Required department. |
| 16 | `JobTitle VARCHAR(80)` | Optional job title. |
| 17 | `DateJoined DATE NOT NULL` | Required join date. |
| 18 | `AnnualLeaveBalance INTEGER DEFAULT 20` | Days left; default 20 if not set. |
| 21 | `CREATE TABLE LeaveTypes (` | Start leave types table. |
| 22 | `LeaveTypeID INTEGER PRIMARY KEY AUTOINCREMENT` | Unique leave-type ID. |
| 23 | `TypeName VARCHAR(50) NOT NULL` | Name e.g. Annual Leave. |
| 24 | `MaxDaysAllowed INTEGER NOT NULL` | Yearly max for that type. |
| 27 | `CREATE TABLE LeaveApplications (` | Start applications table. |
| 28 | `ApplicationID INTEGER PRIMARY KEY AUTOINCREMENT` | Unique application ID. |
| 29 | `EmployeeID INTEGER NOT NULL` | Who applied (must exist in Employees). |
| 30 | `LeaveTypeID INTEGER NOT NULL` | Which leave type (must exist in LeaveTypes). |
| 31–32 | `StartDate` / `EndDate` | Required leave dates. |
| 33 | `NumberOfDays INTEGER NOT NULL` | Days counted for this request. |
| 34 | `Reason TEXT` | Optional reason text. |
| 35–36 | `Status ... CHECK (...)` | Default Pending; only Pending/Approved/Rejected/Cancelled. |
| 37 | `ApprovedBy VARCHAR(100)` | Who approved (can be empty). |
| 38–40 | `FOREIGN KEY (EmployeeID)...` | App must point to a real employee; block delete of that employee. |
| 41–43 | `FOREIGN KEY (LeaveTypeID)...` | App must point to a real leave type. |

**Data flow:** Running this script creates empty tables. Later `INSERT`s fill them; FKs reject bad IDs.
