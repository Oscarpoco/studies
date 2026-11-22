# SLMS Nexus Staff Leave Management System

Student project for **Occupational Certificate: Software Developer (SAQA ID 118707)**.

Built with **Python** and **SQLite3** on **Windows**.

## Project structure

```
slms-nexus/
├── database/   SQL schema, seed data, report queries
├── src/        Application code (one folder per module)
├── tests/      Unit and integration tests
├── docs/       Short planning / debugging notes
└── scripts/    Setup helpers
```

Each file/function lives in its own folder with a `README.md` beside it. Those READMEs explain **every line** and **how data is read or written**.

## Install SQLite3 (Windows)

Python already includes the `sqlite3` module. You still need the SQLite tools for running `.sql` files by hand.

1. Download from https://www.sqlite.org/download.html (**Precompiled Binaries for Windows**).
2. Unzip `sqlite-tools-win-*.zip` (e.g. to `C:\sqlite`).
3. Add that folder to PATH: **Settings → System → About → Advanced system settings → Environment Variables → Path → Edit → New**.
4. Open a **new** Command Prompt or PowerShell and check:
   ```powershell
   sqlite3 --version
   ```

## Setup (Windows)

Open PowerShell or Command Prompt in the project folder:

```powershell
cd slms-nexus
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts\init_db\init_db.py
```

## Run the app

```powershell
python -m src.app.app
```

Open http://127.0.0.1:5000 in your browser.

## Run tests

```powershell
python -m pytest tests\ -v
```

## Theory cheat sheet (PDF)

Open: `docs\cheat_sheet\SLMS_Cheat_Sheet.pdf`

Covers SELECT/CREATE/JOIN, keys, app functions, unit vs integration tests, Git, and “what to use / why”.

Rebuild (optional):

```powershell
python docs\cheat_sheet\build_cheat_sheet.py
```

## Modules

| Folder | Purpose |
|--------|---------|
| `database/` | Tables, sample data, SQL reports |
| `src/db_connection/` | Connect to `SLMS_Nexus.db` |
| `src/calculate_working_days/` | Count Mon–Fri days |
| `src/leave_application/` | Submit leave + balance checks |
| `src/low_balance_employees/` | Warn on low leave balance |
| `src/app/` | Flask Leave Application screen |
| `tests/` | Unit + integration tests |
| `docs/cheat_sheet/` | Theory PDF for students |