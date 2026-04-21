import sqlite3
from exceptions.employee_exceptions import *

class Company:
    def __init__(self):
        self.conn = sqlite3.connect("employee_management.db")
        self.cursor = self.conn.cursor()

    def add_employee(self, emp):
        try:
            self.cursor.execute("SELECT * FROM employees WHERE id=?", (emp.emp_id,))
            if self.cursor.fetchone():
                raise DuplicateEmployeeError()

            self.cursor.execute(
                "INSERT INTO employees VALUES (?, ?, ?, ?, ?)",
                (emp.emp_id, emp.name, emp.age, emp.email, emp.role)
            )
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_employee(self, emp_id):
        self.cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
        emp = self.cursor.fetchone()
        if not emp:
            raise EmployeeNotFoundError()
        return emp

    def assign_project(self, emp_id, project):
        self.cursor.execute("SELECT COUNT(*) FROM projects WHERE emp_id=?", (emp_id,))
        count = self.cursor.fetchone()[0]

        if count >= 5:
            raise ProjectAllocationError()

        self.cursor.execute(
            "INSERT INTO projects (emp_id, project_name) VALUES (?, ?)",
            (emp_id, project)
        )
        self.conn.commit()