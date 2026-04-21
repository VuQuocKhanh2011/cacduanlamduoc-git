class InvalidAgeError(Exception):
    def __str__(self):
        return "Tuổi phải từ 18 đến 65"

class InvalidSalaryError(Exception):
    def __str__(self):
        return "Lương phải > 0"

class EmployeeNotFoundError(Exception):
    def __str__(self):
        return "Không tìm thấy nhân viên"

class ProjectAllocationError(Exception):
    def __str__(self):
        return "Nhân viên đã có 5 dự án"

class DuplicateEmployeeError(Exception):
    def __str__(self):
        return "ID đã tồn tại"