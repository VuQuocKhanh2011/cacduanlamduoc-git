import sqlite3

def create_database():
    conn = sqlite3.connect("employee_management.db")
    cursor = conn.cursor()

    # ⚠️ Bật khóa ngoại (rất quan trọng)
    cursor.execute("PRAGMA foreign_keys = ON")

    # ===== BẢNG NHÂN VIÊN =====
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER CHECK(age >= 18 AND age <= 65),
        email TEXT UNIQUE NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # ===== BẢNG LƯƠNG (có lịch sử) =====
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS salary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id TEXT NOT NULL,
        base_salary REAL CHECK(base_salary > 0),
        bonus REAL DEFAULT 0,
        total_salary REAL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(emp_id) REFERENCES employees(id) ON DELETE CASCADE
    )
    """)

    # ===== BẢNG DỰ ÁN =====
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id TEXT NOT NULL,
        project_name TEXT NOT NULL,
        assigned_date TEXT DEFAULT CURRENT_DATE,
        FOREIGN KEY(emp_id) REFERENCES employees(id) ON DELETE CASCADE
    )
    """)

    # ===== BẢNG ĐÁNH GIÁ =====
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS performance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id TEXT NOT NULL,
        score REAL CHECK(score >= 0 AND score <= 10),
        comment TEXT,
        review_date TEXT DEFAULT CURRENT_DATE,
        FOREIGN KEY(emp_id) REFERENCES employees(id) ON DELETE CASCADE
    )
    """)

    # ===== INDEX (tăng tốc tìm kiếm) =====
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_salary_emp ON salary(emp_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_project_emp ON projects(emp_id)")

    conn.commit()
    conn.close()

    print("✅ Database FULL đã tạo xong!")

if __name__ == "__main__":
    create_database()