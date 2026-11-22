# app.py — line by line

Flask Leave Application screen; loads dropdown data and posts leave.

| Line | Code | What it does |
|------|------|--------------|
| 3 | `Path` | Locate templates folder. |
| 5 | Flask imports | App, HTML render, form data. |
| 7–8 | Local imports | DB connect + `leaveApplication`. |
| 10 | `TEMPLATE_DIR` | Points to `src/templates`. |
| 12 | `app = Flask(...)` | Create web app using that template folder. |
| 15 | `_load_form_options()` | Helper to fill dropdowns. |
| 16 | `connect_database()` | Open main DB. |
| 18–21 | `SELECT ... FROM Employees ORDER BY LastName` | All staff for Employee dropdown (id, name, balance). |
| 22–24 | `SELECT ... FROM LeaveTypes` | All leave types for Leave Type dropdown. |
| 25 | `return list(...), list(...)` | Two lists for the template. |
| 26–27 | `finally: close` | Close after reads. |
| 30 | `@app.route("/", GET/POST)` | `/` handles page load and form submit. |
| 32–33 | `message` / `success` | Empty until a POST. |
| 35 | `if request.method == "POST"` | User clicked Submit. |
| 36–42 | `leaveApplication(...)` | Read form fields → run leave logic → get result. |
| 43–44 | Set message flags | From result dict for on-screen feedback. |
| 46 | Reload options | Fresh balances after submit. |
| 47–53 | `render_template(...)` | Build HTML with employees, types, message. |
| 56–57 | `main()` | Start server on 127.0.0.1:5000. |
| 60–61 | `__main__` | `python -m src.app.app` runs the server. |

**Data flow:** Browser GET → SQL loads dropdowns → HTML. POST → form values → `leaveApplication` reads/writes DB → page reloads with message.
