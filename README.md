# Employee Management System

A lightweight employee management web application built with Flask and SQLite. It provides a browser-based interface for adding, viewing, searching, updating, and deleting employee records.

## Technologies and tools

- Python 3
- Flask
- SQLite
- HTML, CSS, and JavaScript
- Git and GitHub

## Features

- Add employee records
- View all employees
- Search by employee ID, name, or department
- Update employee details
- Delete employee records
- SQLite database created automatically on first run

## Run locally

1. Clone the repository and open the project directory:

   ```bash
   git clone https://github.com/Vansh18-Coder/TA_MDM_Employee_Management_System.git
   cd TA_MDM_Employee_Management_System
   ```

2. Create and activate a virtual environment (recommended):

   Windows PowerShell:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python app.py
   ```

5. Open http://127.0.0.1:5000 in a browser.

The SQLite database file (`employees.db`) is generated locally when the application starts and is intentionally excluded from version control.

