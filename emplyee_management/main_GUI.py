import sys
from PyQt6 import QtWidgets
from main import Ui_Dialog
import sqlite3


class MainApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.conn = sqlite3.connect("employee_management.db")
        self.cursor = self.conn.cursor()

        self.selected_id = None

        # ===== PAGINATION =====
        self.current_page = 0
        self.page_size = 5
        self.all_data = []

        self.init_table()

        # ===== EVENTS =====
        self.ui.tableWidget.cellClicked.connect(self.select_employee)

        self.ui.pushButton.clicked.connect(self.add_employee)
        self.ui.pushButton_2.clicked.connect(self.update_employee)
        self.ui.pushButton_3.clicked.connect(self.delete_employee)
        self.ui.pushButton_4.clicked.connect(self.calc_salary)
        self.ui.pushButton_5.clicked.connect(self.assign_project)

        self.btnPrev = QtWidgets.QPushButton("<< Trang trước", self)
        self.btnPrev.setGeometry(350, 650, 120, 30)

        self.btnNext = QtWidgets.QPushButton("Trang sau >>", self)
        self.btnNext.setGeometry(500, 650, 120, 30)

        self.lblPage = QtWidgets.QLabel(self)
        self.lblPage.setGeometry(650, 650, 150, 30)

        # connect
        self.btnNext.clicked.connect(self.next_page)
        self.btnPrev.clicked.connect(self.prev_page)

        self.load_data()

    # ===== TABLE =====
    def init_table(self):
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Tên", "Tuổi", "Email", "Chức vụ", "Dự án", "Lương gần nhất"]
        )

    # ===== LOAD DATA =====
    def load_data(self):
        self.cursor.execute("SELECT * FROM employees")
        self.all_data = self.cursor.fetchall()

        self.current_page = 0
        self.show_page()

    # ===== SHOW PAGE =====
    def show_page(self):
        start = self.current_page * self.page_size
        end = start + self.page_size
        data = self.all_data[start:end]

        self.ui.tableWidget.setRowCount(len(data))

        for row, emp in enumerate(data):
            emp_id = emp[0]

            # PROJECT
            self.cursor.execute("SELECT project_name FROM projects WHERE emp_id=?", (emp_id,))
            projects = [p[0] for p in self.cursor.fetchall()]
            project_text = ", ".join(projects) if projects else "NULL"

            # SALARY
            self.cursor.execute("""
                SELECT total_salary FROM salary 
                WHERE emp_id=? ORDER BY id DESC LIMIT 1
            """, (emp_id,))
            sal = self.cursor.fetchone()
            salary_text = str(sal[0]) if sal else "NULL"

            full_data = list(emp) + [project_text, salary_text]

            for col, val in enumerate(full_data):
                self.ui.tableWidget.setItem(
                    row, col, QtWidgets.QTableWidgetItem(str(val))
                )

    # ===== NEXT / PREV =====
    def next_page(self):
        if (self.current_page + 1) * self.page_size < len(self.all_data):
            self.current_page += 1
            self.show_page()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.show_page()

    # ===== SELECT =====
    def select_employee(self, row, column):
        self.selected_id = self.ui.tableWidget.item(row, 0).text()

        self.ui.lineEdit.setText(self.selected_id)
        self.ui.lineEdit_2.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.lineEdit_3.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.lineEdit_4.setText(self.ui.tableWidget.item(row, 3).text())
        self.ui.lineEdit_5.setText(self.ui.tableWidget.item(row, 4).text())

    # ===== ADD =====
    def add_employee(self):
        try:
            id = self.ui.lineEdit.text()
            name = self.ui.lineEdit_2.text()
            age = int(self.ui.lineEdit_3.text())
            email = self.ui.lineEdit_4.text()
            role = self.ui.lineEdit_5.text()

            self.cursor.execute("""
                INSERT INTO employees (id, name, age, email, role)
                VALUES (?, ?, ?, ?, ?)
            """, (id, name, age, email, role))

            self.conn.commit()
            self.load_data()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", str(e))

    # ===== UPDATE =====
    def update_employee(self):
        try:
            if not self.selected_id:
                raise Exception("Chọn nhân viên")

            self.cursor.execute("""
                UPDATE employees
                SET name=?, age=?, email=?, role=?
                WHERE id=?
            """, (
                self.ui.lineEdit_2.text(),
                int(self.ui.lineEdit_3.text()),
                self.ui.lineEdit_4.text(),
                self.ui.lineEdit_5.text(),
                self.selected_id
            ))

            self.conn.commit()
            self.load_data()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", str(e))

    # ===== DELETE =====
    def delete_employee(self):
        try:
            if not self.selected_id:
                raise Exception("Chọn nhân viên")

            self.cursor.execute("DELETE FROM employees WHERE id=?", (self.selected_id,))
            self.conn.commit()

            self.load_data()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", str(e))

    # ===== SALARY =====
    def calc_salary(self):
        try:
            if not self.selected_id:
                raise Exception("Chọn nhân viên")

            base = float(self.ui.lineEdit_7.text())
            bonus = float(self.ui.lineEdit_8.text())

            total = base + bonus

            self.cursor.execute("""
                INSERT INTO salary (emp_id, base_salary, bonus, total_salary)
                VALUES (?, ?, ?, ?)
            """, (self.selected_id, base, bonus, total))

            self.conn.commit()

            QtWidgets.QMessageBox.information(self, "Lương", f"Tổng lương: {total}")
            self.load_data()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", str(e))

    # ===== PROJECT =====
    def assign_project(self):
        try:
            if not self.selected_id:
                raise Exception("Chọn nhân viên")

            project = self.ui.lineEdit_9.text().strip()

            if project == "":
                raise Exception("Tên dự án không được để trống")

            self.cursor.execute(
                "SELECT COUNT(*) FROM projects WHERE emp_id=?", (self.selected_id,)
            )
            if self.cursor.fetchone()[0] >= 5:
                raise Exception("Tối đa 5 dự án")

            self.cursor.execute("""
                INSERT INTO projects (emp_id, project_name)
                VALUES (?, ?)
            """, (self.selected_id, project))

            self.conn.commit()

            QtWidgets.QMessageBox.information(self, "OK", "Đã thêm dự án")

            self.ui.lineEdit_9.clear()
            self.load_data()

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", str(e))


# ===== RUN =====
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())