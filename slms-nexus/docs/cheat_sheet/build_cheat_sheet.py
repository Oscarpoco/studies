"""Build SLMS theory cheat sheet PDF for students."""

from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent / "SLMS_Cheat_Sheet.pdf"


class CheatPDF(FPDF):
    def _reset_x(self) -> None:
        self.set_x(self.l_margin)

    def header(self) -> None:
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(90, 90, 90)
        self.cell(0, 6, "SLMS Nexus - Theory Cheat Sheet (SAQA 118707)", align="L")
        self.ln(8)
        self._reset_x()

    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Page {self.page_no()}/{{nb}}", align="C")

    def h1(self, text: str) -> None:
        self._reset_x()
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(11, 110, 79)
        self.multi_cell(0, 8, text)
        self.ln(2)
        self._reset_x()

    def h2(self, text: str) -> None:
        self.ln(2)
        self._reset_x()
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(26, 43, 60)
        self.multi_cell(0, 7, text)
        self.ln(1)
        self._reset_x()

    def h3(self, text: str) -> None:
        self._reset_x()
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(40, 60, 80)
        self.multi_cell(0, 6, text)
        self.ln(0.5)
        self._reset_x()

    def body(self, text: str) -> None:
        self._reset_x()
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5, text)
        self.ln(1)
        self._reset_x()

    def bullet(self, title: str, text: str) -> None:
        self._reset_x()
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(30, 30, 30)
        label = f"- {title}: "
        self.set_font("Helvetica", "", 9)
        self.multi_cell(0, 5, f"{label}{text}")
        self._reset_x()

    def code(self, text: str) -> None:
        self._reset_x()
        self.set_fill_color(240, 244, 248)
        self.set_font("Courier", "", 8)
        self.set_text_color(20, 20, 20)
        self.multi_cell(0, 4.5, text, fill=True)
        self.ln(2)
        self._reset_x()

    def tip(self, text: str) -> None:
        self._reset_x()
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(11, 110, 79)
        self.multi_cell(0, 5, f"Why / tip: {text}")
        self.ln(1)
        self._reset_x()

    def center_line(self, text: str, size: int = 10, bold: bool = False) -> None:
        self._reset_x()
        style = "B" if bold else ""
        self.set_font("Helvetica", style, size)
        self.multi_cell(0, 6, text, align="C")
        self._reset_x()


def build() -> Path:
    pdf = CheatPDF(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=16)
    pdf.add_page()

    # Cover
    pdf.ln(20)
    pdf.set_text_color(11, 110, 79)
    pdf.center_line("SLMS Nexus", size=22, bold=True)
    pdf.set_text_color(26, 43, 60)
    pdf.center_line("Theory Cheat Sheet for Students", size=14, bold=True)
    pdf.ln(4)
    pdf.set_text_color(60, 60, 60)
    pdf.center_line("Staff Leave Management System")
    pdf.center_line("Occupational Certificate: Software Developer (SAQA ID 118707)")
    pdf.center_line("What to use, how it works, and why it matters.")
    pdf.ln(8)
    pdf.set_text_color(26, 43, 60)
    pdf.center_line("Inside this guide", size=11, bold=True)
    pdf.set_text_color(60, 60, 60)
    for item in [
        "1. Databases & SQLite basics",
        "2. SQL commands (CREATE, SELECT, INSERT, JOIN...)",
        "3. Keys, constraints & data integrity",
        "4. Application logic (functions & flow)",
        "5. Unit tests vs integration tests",
        "6. Debugging, Git & exam tips",
    ]:
        pdf.center_line(item)

    # 1
    pdf.add_page()
    pdf.h1("1. Databases & SQLite - the big idea")
    pdf.body(
        "A database stores structured data in tables (rows and columns). "
        "Your SLMS system needs Employees, LeaveTypes, and LeaveApplications."
    )
    pdf.bullet("Table", "A grid of related data (like a spreadsheet sheet).")
    pdf.bullet("Row / record", "One item (one employee, one leave application).")
    pdf.bullet("Column / field", "One attribute (Email, Status, StartDate).")
    pdf.bullet("SQL", "The language used to create tables and ask questions of data.")
    pdf.bullet("SQLite", "A lightweight database stored in one file (SLMS_Nexus.db).")
    pdf.tip(
        "Use SQLite for learning and small apps. No separate server install is required "
        "for Python's sqlite3 module - the .db file is the database."
    )
    pdf.h2("When do you use a database?")
    pdf.body(
        "When data must survive after the program closes, be shared by many screens, "
        "and stay consistent (e.g. leave balance must match approved leave)."
    )
    pdf.h2("SLMS tables (theory map)")
    pdf.body(
        "Employees = who works here.\n"
        "LeaveTypes = what kinds of leave exist (Annual, Sick, Family).\n"
        "LeaveApplications = each request linking an employee + a leave type."
    )
    pdf.tip(
        "One employee can have many applications. One leave type can appear on many "
        "applications. That is a one-to-many relationship."
    )

    # 2
    pdf.add_page()
    pdf.h1("2. SQL commands cheat sheet")

    pdf.h2("CREATE TABLE - define structure")
    pdf.body(
        "Use when you need a new table. You decide column names, types, and rules "
        "before any data is stored."
    )
    pdf.code(
        "CREATE TABLE Employees (\n"
        "  EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,\n"
        "  FirstName VARCHAR(50) NOT NULL,\n"
        "  Email VARCHAR(100) NOT NULL UNIQUE\n"
        ");"
    )
    pdf.tip("CREATE builds the empty container. It does not insert people yet.")

    pdf.h2("DROP TABLE - remove a table")
    pdf.body("Deletes the table and all its data. Use carefully; often in setup scripts only.")
    pdf.code("DROP TABLE IF EXISTS LeaveApplications;")
    pdf.tip("IF EXISTS avoids an error if the table is already gone. Drop child tables first.")

    pdf.h2("INSERT - add data")
    pdf.body("Use when capturing a new record (new employee, new leave request).")
    pdf.code(
        "INSERT INTO Employees (FirstName, LastName, Email, Department, DateJoined)\n"
        "VALUES ('Thabo', 'Molefe', 'thabo@nexus.co.za', 'Finance', '2021-03-15');"
    )
    pdf.tip("List columns, then VALUES. AutoIncrement IDs are filled by SQLite.")

    pdf.h2("SELECT - read / report data")
    pdf.body(
        "Use when you need to display or report information. SELECT never changes data; "
        "it only retrieves it."
    )
    pdf.code(
        "SELECT EmployeeID, FirstName, LastName, AnnualLeaveBalance\n"
        "FROM Employees\n"
        "ORDER BY AnnualLeaveBalance ASC;"
    )
    pdf.bullet("SELECT columns", "Which fields to show.")
    pdf.bullet("FROM table", "Where the rows live.")
    pdf.bullet("WHERE condition", "Filter rows (e.g. Status = 'Pending').")
    pdf.bullet("ORDER BY", "Sort ASC (low to high) or DESC (high to low).")
    pdf.bullet("GROUP BY + SUM", "Totals per group (e.g. days per department).")

    pdf.h2("UPDATE - change existing rows")
    pdf.body("Use when a value must change (e.g. reduce leave balance after submit).")
    pdf.code(
        "UPDATE Employees\n"
        "SET AnnualLeaveBalance = 15\n"
        "WHERE EmployeeID = 1;"
    )
    pdf.tip("Always use WHERE. Without WHERE, every row updates.")

    pdf.h2("DELETE - remove rows")
    pdf.body("Use when a record should no longer exist. Prefer careful WHERE filters.")
    pdf.code("DELETE FROM LeaveApplications WHERE ApplicationID = 9;")

    # 3 JOIN etc
    pdf.add_page()
    pdf.h1("3. Filtering, joining & aggregating")

    pdf.h2("WHERE - keep only matching rows")
    pdf.code("SELECT * FROM LeaveApplications WHERE Status = 'Pending';")
    pdf.tip("Compare text in quotes. Numbers without quotes. Operators: =, <, >, <=, >=, <> .")

    pdf.h2("INNER JOIN - combine related tables")
    pdf.body(
        "Use when one table alone is not enough. Example: approved days live in "
        "LeaveApplications, department lives in Employees - join on EmployeeID."
    )
    pdf.code(
        "SELECT e.Department, SUM(la.NumberOfDays) AS TotalApprovedDays\n"
        "FROM LeaveApplications la\n"
        "INNER JOIN Employees e ON la.EmployeeID = e.EmployeeID\n"
        "WHERE la.Status = 'Approved'\n"
        "GROUP BY e.Department\n"
        "ORDER BY TotalApprovedDays DESC;"
    )
    pdf.bullet("ON ...", "The matching rule (foreign key = primary key).")
    pdf.bullet("INNER JOIN", "Only rows that match in both tables.")
    pdf.bullet("SUM(...)", "Adds numbers in the group.")
    pdf.bullet("AS alias", "Gives the result column a clear name.")
    pdf.tip(
        "Think: applications know EmployeeID; employees know Department. "
        "JOIN stitches those facts together for reporting."
    )

    pdf.h2("Aliases (e / la)")
    pdf.body(
        "Short names for tables in a query. They keep SQL shorter and avoid "
        "confusion when both tables have similar column names."
    )

    pdf.h1("4. Keys, constraints & integrity")
    pdf.h2("PRIMARY KEY")
    pdf.body(
        "Unique ID for each row (EmployeeID, ApplicationID). "
        "AUTOINCREMENT means SQLite assigns the next number."
    )
    pdf.h2("FOREIGN KEY")
    pdf.body(
        "A column that must point to a real row in another table. "
        "LeaveApplications.EmployeeID must exist in Employees."
    )
    pdf.tip(
        "This is validation: you cannot save a leave application for a fake employee. "
        "In SQLite turn it on with: PRAGMA foreign_keys = ON;"
    )
    pdf.h2("NOT NULL / UNIQUE / DEFAULT / CHECK")
    pdf.bullet("NOT NULL", "Field required.")
    pdf.bullet("UNIQUE", "No duplicates (Email).")
    pdf.bullet("DEFAULT", "Value used if none given (Status default 'Pending').")
    pdf.bullet("CHECK", "Only allowed values (Pending, Approved, Rejected, Cancelled).")
    pdf.tip(
        "Constraints protect data quality so the app logic does not rely only on hope."
    )

    # 4 App logic
    pdf.add_page()
    pdf.h1("5. Application logic - how & why")

    pdf.h2("Function")
    pdf.body(
        "A named block of code that takes inputs and returns a result. "
        "Reuse it from the web form, tests, or other modules."
    )

    pdf.h2("calculateWorkingDays(startDate, endDate)")
    pdf.body(
        "Business need: leave days should count Mon-Fri only (weekends off). "
        "Public holidays are a later enhancement; this function handles weekdays."
    )
    pdf.bullet("How", "Walk each day from start to end; if weekday, add 1.")
    pdf.bullet("Why return 0", "End before start is invalid - safe failure.")
    pdf.tip("Pure logic: no database. Easy to unit test with fixed dates.")

    pdf.h2("leaveApplication(...)")
    pdf.body(
        "Business need: staff request leave safely. System must check balance, "
        "save the request, and update remaining days."
    )
    pdf.body(
        "Typical flow:\n"
        "1) Count working days\n"
        "2) SELECT employee balance\n"
        "3) If not enough days -> reject + show balance\n"
        "4) Else INSERT application Status='Pending'\n"
        "5) UPDATE employee balance\n"
        "6) COMMIT and return success message"
    )
    pdf.tip(
        "Separate 'calculate days' from 'save leave' so each piece is testable and clear."
    )

    pdf.h2("getLowBalanceEmployees()")
    pdf.body(
        "Reporting helper: SELECT employees with AnnualLeaveBalance <= 5, "
        "then warn HR. Theory lesson: SQL bugs (missing spaces, wrong operator =<) "
        "break queries - always check syntax carefully."
    )

    pdf.h2("Pseudocode & algorithms")
    pdf.bullet("Pseudocode", "Human steps before real code. Plans inputs, decisions, outputs.")
    pdf.bullet("Algorithm", "Ordered steps that always finish with a clear result.")
    pdf.tip("Examiners want evidence you planned first - then coded.")

    # Testing
    pdf.add_page()
    pdf.h1("6. Testing theory - unit vs integration")

    pdf.h2("Why test at all?")
    pdf.body(
        "A leave system that miscounts days or steals balance hurts people. "
        "Tests prove a function behaves as expected before you trust it in production."
    )

    pdf.h2("Unit test")
    pdf.bullet("What", "Tests one function in isolation.")
    pdf.bullet("Example", "calculateWorkingDays with known dates -> expect 5.")
    pdf.bullet("Data", "Usually no real database - only inputs you control.")
    pdf.bullet("Tool (Python)", "pytest or unittest.")
    pdf.code(
        "def test_five_weekdays():\n"
        "    assert calculateWorkingDays('2026-03-02', '2026-03-06') == 5"
    )
    pdf.tip(
        "Unit tests are fast and pinpoint the exact function that broke."
    )

    pdf.h2("Integration test")
    pdf.bullet("What", "Tests several parts working together.")
    pdf.bullet("Example", "leaveApplication writes to SQLite and balance drops.")
    pdf.bullet("Checks", "Row saved, Status=Pending, balance updated, error if insufficient.")
    pdf.bullet("Data", "Often a temporary test database, not the live student DB.")
    pdf.tip(
        "Integration tests catch wiring bugs: SQL OK alone, function OK alone, "
        "but together they fail."
    )

    pdf.h2("Pass / Fail table mindset")
    pdf.body(
        "For each case write: Test case | Expected | Actual | Pass/Fail. "
        "If fail: what went wrong, what you change, re-run."
    )

    pdf.h2("Common test cases for working days")
    pdf.body(
        "1) Five weekdays in a row -> 5\n"
        "2) Range crossing weekends -> only weekdays counted\n"
        "3) Same start and end weekday -> 1\n"
        "4) End before start -> 0 (or handled error)"
    )

    # Git + exam
    pdf.add_page()
    pdf.h1("7. Git basics (why version control)")
    pdf.body(
        "Git stores history of your project. You can branch, commit, and push safely."
    )
    pdf.bullet("clone", "Copy a remote repo to your PC.")
    pdf.bullet("branch", "Work on changes without breaking main.")
    pdf.bullet("commit", "Save a snapshot with a message.")
    pdf.bullet("push", "Upload your branch to GitHub/remote.")
    pdf.tip("Commit often with clear messages. Screenshots of these steps are often required.")

    pdf.h1("8. Quick 'what should I use?' guide")
    pdf.body(
        "Need a new table structure? -> CREATE TABLE\n"
        "Need sample or new rows? -> INSERT\n"
        "Need a report / list on screen? -> SELECT (+ WHERE / JOIN / ORDER BY)\n"
        "Need to change a balance or status? -> UPDATE\n"
        "Need to remove a row? -> DELETE\n"
        "Need to stop fake employee IDs? -> FOREIGN KEY + PRAGMA foreign_keys=ON\n"
        "Need to count Mon-Fri only? -> calculateWorkingDays function\n"
        "Need to submit leave safely? -> leaveApplication function\n"
        "Need to prove one function works? -> Unit test\n"
        "Need to prove DB + logic work together? -> Integration test\n"
        "Need to plan before coding? -> Pseudocode / flowchart\n"
        "Need history / teamwork on code? -> Git branch + commit + push"
    )

    pdf.h1("9. Exam / practical tips")
    pdf.body(
        "- Read the data dictionary - use exact field names.\n"
        "- Screenshot query + results when asked.\n"
        "- Comment your code briefly (what / why).\n"
        "- Test edge cases (same day, weekend span, insufficient balance).\n"
        "- If a test fails, fix the code, then re-run - write what you changed.\n"
        "- Keep Status values exact: Pending, Approved, Rejected, Cancelled.\n"
        "- NumberOfDays should match the business rule (working days)."
    )
    pdf.ln(4)
    pdf._reset_x()
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(11, 110, 79)
    pdf.multi_cell(0, 6, "Remember: tools answer 'how'. Requirements answer 'why'.")
    pdf._reset_x()
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        5,
        "Always connect each SQL command or function back to a business need "
        "(HR report, valid leave request, data integrity).",
    )
    pdf._reset_x()

    pdf.output(OUT)
    return OUT


if __name__ == "__main__":
    path = build()
    print(f"Created: {path}")
