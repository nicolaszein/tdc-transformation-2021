from src.infrastructure.sqlalchemy import Employee, session
from src.domain.employee_repository import EmployeeRepository as AbstractEmployeeRepository


class EmployeeRepository(AbstractEmployeeRepository):

    def fetch_by_id(self, id):
        employee = session.query(Employee).filter(Employee.id == id).first()

        return employee.to_domain() if employee else None

    def create(self, employee):
        employee_model = Employee.from_domain(employee)
        try:
            session.add(employee_model)
            session.commit()

            return employee_model.to_domain()
        except Exception as e:
            session.rollback()
            raise e
