# Task 2.2 — five errors

| # | Line / Section | Error Type | What the Error Is | How to Fix It |
|---|----------------|------------|-------------------|---------------|
| 1 | query + "FROM Employees" | Syntax | Missing space before FROM | Use `" FROM Employees"` |
| 2 | WHERE ... =< 5 | Operator | `=<` is invalid | Use `<= 5` |
| 3 | IF results.count = 0 | Logic / syntax | Single `=` and may need THEN | Use `== 0` / proper IF |
| 4 | PRINTER "WARNING..." | Typo | `PRINTER` is not valid | Use `PRINT` |
| 5 | conn.close | Incomplete call | Missing parentheses | Use `conn.close()` |
