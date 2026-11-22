-- Q1 report queries for SLMS_Nexus

-- 1.1.1 (1) Employees ordered by leave balance (lowest to highest)
SELECT EmployeeID, FirstName, LastName, Email, AnnualLeaveBalance
FROM Employees
ORDER BY AnnualLeaveBalance ASC;

-- 1.1.1 (2) Pending leave applications
SELECT ApplicationID, EmployeeID, StartDate, EndDate, NumberOfDays, Reason
FROM LeaveApplications
WHERE Status = 'Pending';

-- 1.1.1 (3) Total approved leave days per department (highest to lowest)
SELECT e.Department, SUM(la.NumberOfDays) AS TotalApprovedDays
FROM LeaveApplications la
INNER JOIN Employees e ON la.EmployeeID = e.EmployeeID
WHERE la.Status = 'Approved'
GROUP BY e.Department
ORDER BY TotalApprovedDays DESC;
