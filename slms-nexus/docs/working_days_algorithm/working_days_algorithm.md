# calculateWorkingDays(startDate, endDate)

1. Convert both inputs to dates  
2. If endDate < startDate → return 0  
3. Set count = 0 and current = startDate  
4. While current ≤ endDate:  
   - If current is Mon–Fri → count = count + 1  
   - Move current to next day  
5. Return count  
