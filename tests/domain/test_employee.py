import unittest
from src.domain.employee import Employee


class TestEmployee(unittest.TestCase):

    def test_employee_update_role(self):
        employee = Employee(name='Miguel', role='Software Engineer I')

        updated_employee = employee.update_role(new_role='Software Engineer II')

        self.assertEqual(updated_employee.role, 'Software Engineer II')
