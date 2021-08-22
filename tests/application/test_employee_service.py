import unittest
from unittest.mock import MagicMock
from src.domain.employee_repository import EmployeeRepository
from src.application.employee_service import EmployeeService


class TestEmployee(unittest.TestCase):

    def test_fetch_by_id(self):
        repository = MagicMock(spec=EmployeeRepository)
        employee = MagicMock()
        employee_service = EmployeeService(employee_repository=repository)

        repository.fetch_by_id.return_value = employee

        result = employee_service.fetch_by_id(id='employee-id')

        self.assertEqual(result, employee)

    def test_create(self):
        repository = MagicMock(spec=EmployeeRepository)
        employee_service = EmployeeService(employee_repository=repository)

        repository.create.side_effect = lambda x: x

        employee = employee_service.create(name='Luisa', role='Product Manager')

        self.assertEqual(employee.name, 'Luisa')
        self.assertEqual(employee.role, 'Product Manager')
