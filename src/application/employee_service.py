from src.domain.employee import Employee
from src.domain.employee_repository import EmployeeRepository


class EmployeeService:

    def __init__(self, employee_repository: EmployeeRepository):
        self.__employee_repository = employee_repository

    def fetch_by_id(self, id):
        return self.__employee_repository.fetch_by_id(id)

    def create(self, name, role):
        employee = Employee(
            name=name,
            role=role
        )
        return self.__employee_repository.create(employee)
