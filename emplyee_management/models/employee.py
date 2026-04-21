class Employee:
    def __init__(self, emp_id, name, age, email, role):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.role = role

    def __str__(self):
        return f"{self.emp_id} - {self.name} - {self.role}"