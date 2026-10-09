from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

DATABASE = "employees.db"


# Database connection
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create table
def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            designation TEXT NOT NULL,
            salary REAL NOT NULL,
            contact TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# GET - View all employees
@app.route("/employees", methods=["GET"])
def get_employees():

    conn = get_db()

    employees = conn.execute(
        "SELECT * FROM employees"
    ).fetchall()

    conn.close()

    return jsonify([dict(emp) for emp in employees])


# POST - Add employee
@app.route("/employees", methods=["POST"])
def add_employee():

    data = request.json

    try:
        conn = get_db()

        conn.execute("""
            INSERT INTO employees
            (employee_id, name, department, designation, salary, contact)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data["employee_id"],
            data["name"],
            data["department"],
            data["designation"],
            data["salary"],
            data["contact"]
        ))

        conn.commit()
        conn.close()

        return jsonify({"message": "Employee added successfully"}), 201

    except sqlite3.IntegrityError:

        return jsonify({"error": "Employee ID already exists"}), 400


# GET - Search employees
@app.route("/employees/search", methods=["GET"])
def search_employee():

    keyword = request.args.get("keyword", "")

    conn = get_db()

    employees = conn.execute("""
        SELECT * FROM employees
        WHERE employee_id LIKE ?
        OR name LIKE ?
        OR department LIKE ?
    """, (
        "%" + keyword + "%",
        "%" + keyword + "%",
        "%" + keyword + "%"
    )).fetchall()

    conn.close()

    return jsonify([dict(emp) for emp in employees])


# PUT - Update employee
@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):

    data = request.json

    conn = get_db()

    cursor = conn.execute("""
        UPDATE employees
        SET employee_id = ?,
            name = ?,
            department = ?,
            designation = ?,
            salary = ?,
            contact = ?
        WHERE id = ?
    """, (
        data["employee_id"],
        data["name"],
        data["department"],
        data["designation"],
        data["salary"],
        data["contact"],
        id
    ))

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Employee not found"}), 404

    conn.close()

    return jsonify({"message": "Employee updated successfully"})


# DELETE - Delete employee
@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):

    conn = get_db()

    cursor = conn.execute(
        "DELETE FROM employees WHERE id = ?",
        (id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Employee not found"}), 404

    conn.close()

    return jsonify({"message": "Employee deleted successfully"})


# Start application
if __name__ == "__main__":
    init_db()
    app.run(debug=True)