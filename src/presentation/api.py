from flask import Flask, jsonify, request
from pydantic import BaseModel, ValidationError

from src.presentation import build_employee_service

app = Flask(__name__)


class EmployeeCreationRequest(BaseModel):
    name: str
    role: str


@app.route('/employees', methods=['POST'])
def post_employee():
    try:
        employee_params = EmployeeCreationRequest(**request.json or {})
    except ValidationError as e:
        return jsonify(e.errors())

    employee_service = build_employee_service()
    employee = employee_service.create(
        name=employee_params.name,
        role=employee_params.role
    )

    return jsonify(employee)


@app.route('/employees/<uuid:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee_service = build_employee_service()
    employee = employee_service.fetch_by_id(employee_id)

    if not employee:
        return jsonify(dict(message='Employee not found')), 404

    return jsonify(employee)
