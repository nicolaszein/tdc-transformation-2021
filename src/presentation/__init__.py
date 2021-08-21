from src.application.employee_service import EmployeeService
from src.infrastructure.sqlalchemy.employee_repository import EmployeeRepository


def build_employee_service():
    employee_repository = EmployeeRepository()

    return EmployeeService(employee_repository=employee_repository)
