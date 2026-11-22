-- Sample data for SLMS_Nexus

PRAGMA foreign_keys = ON;

INSERT INTO Employees (FirstName, LastName, Email, Department, JobTitle, DateJoined, AnnualLeaveBalance)
VALUES
    ('Thabo', 'Molefe', 'thabo.molefe@nexus.co.za', 'Finance', 'Accountant', '2021-03-15', 18),
    ('Aisha', 'Patel', 'aisha.patel@nexus.co.za', 'Finance', 'Analyst', '2022-07-01', 12),
    ('Johan', 'van Wyk', 'johan.vanwyk@nexus.co.za', 'IT', 'Developer', '2020-01-10', 20),
    ('Lerato', 'Dlamini', 'lerato.dlamini@nexus.co.za', 'IT', 'Support Lead', '2019-11-20', 5);

INSERT INTO LeaveTypes (TypeName, MaxDaysAllowed)
VALUES
    ('Annual Leave', 21),
    ('Sick Leave', 30),
    ('Family Responsibility Leave', 3);

INSERT INTO LeaveApplications
    (EmployeeID, LeaveTypeID, StartDate, EndDate, NumberOfDays, Reason, Status, ApprovedBy)
VALUES
    (1, 1, '2026-02-02', '2026-02-06', 5, 'Family holiday', 'Approved', 'HR Manager'),
    (2, 2, '2026-03-10', '2026-03-11', 2, 'Flu', 'Pending', NULL),
    (3, 1, '2026-04-06', '2026-04-10', 5, 'Rest break', 'Rejected', 'HR Manager'),
    (4, 3, '2026-01-15', '2026-01-15', 1, 'School meeting', 'Approved', 'HR Manager'),
    (1, 1, '2026-05-04', '2026-05-08', 5, 'Travel', 'Pending', NULL);
