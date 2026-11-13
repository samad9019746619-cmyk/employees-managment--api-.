
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Ali", "department": "IT"},
    {"id": 2, "name": "Ahmed", "department": "HR"}
]


# GET: Retrieve all employees
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees), 200


# POST: Add an employee
@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json(silent=True) or {}

    name = data.get("name")
    department = data.get("department")

    if not name or not department:
        return jsonify({"error": "Name and department are required"}), 400

    new_employee = {
        "id": max([e["id"] for e in employees], default=0) + 1,
        "name": name,
        "department": department
    }

    employees.append(new_employee)

    return jsonify({
        "message": "Employee added successfully",
        "employee": new_employee
    }), 201


# GET: Retrieve one employee
@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(employee), 200


# PUT: Replace all employee details
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json(silent=True) or {}

    if not data.get("name") or not data.get("department"):
        return jsonify({"error": "Name and department are required"}), 400

    employee["name"] = data["name"]
    employee["department"] = data["department"]

    return jsonify({
        "message": "Employee replaced successfully",
        "employee": employee
    }), 200


# PATCH: Update selected employee details
@app.route("/employees/<int:employee_id>", methods=["PATCH"])
def patch_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json(silent=True) or {}

    if not data or any(k not in ["name", "department"] for k in data):
        return jsonify({"error": "Provide name or department only"}), 400

    employee.update(data)

    return jsonify({
        "message": "Employee updated successfully",
        "employee": employee
    }), 200


# DELETE: Remove an employee
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    employees.remove(employee)

    return jsonify({"message": "Employee deleted successfully"}), 200


# HEAD: Return headers without a response body
@app.route("/employees", methods=["HEAD"])
def head_employees():
    response = make_response("", 200)
    response.headers["Content-Type"] = "application/json"
    return response


# OPTIONS: Show supported methods
@app.route("/employees", methods=["OPTIONS"])
def options_employees():
    response = jsonify({
        "allowed_methods": ["GET", "POST", "HEAD", "OPTIONS"]
    })
    response.headers["Allow"] = "GET, POST, HEAD, OPTIONS"
    return response, 200


if __name__ == "__main__":
    app.run(debug=True)
