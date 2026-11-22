# pseudocode_errors.md

Five bugs in Task 2.2 pseudocode vs the fixed `getLowBalanceEmployees` code.

| # | Broken bit | Why it fails | Fix |
|---|------------|--------------|-----|
| 1 | `"FROM Employees"` glued on | SQL becomes `...BalanceFROM` | Space before FROM |
| 2 | `=<` | Invalid operator | Use `<=` |
| 3 | `IF results.count = 0` | Wrong compare / style | Use proper equality |
| 4 | `PRINTER` | Typo | Use `PRINT` |
| 5 | `conn.close` | Not called | Use `conn.close()` |

Fixed query data path: SELECT employees WHERE balance ≤ 5 → print warnings.
