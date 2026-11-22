# leaveApplication — plan

1. Input: EmployeeID, LeaveTypeID, StartDate, EndDate, Reason  
2. Read employee AnnualLeaveBalance  
3. days = calculateWorkingDays(StartDate, EndDate)  
4. If days == 0 → show date error  
5. If balance < days → reject and show balance  
6. Else save application Status = Pending, reduce balance, show success  
