import json
import os

# File path for storing employee data
EMPLOYEE_FILE = 'employees.json'


def load_employee_data():
    if os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, 'r') as file:
            return json.load(file)
    return []


def save_employee_data(employees):
    with open(EMPLOYEE_FILE, 'w') as file:
        json.dump(employees, file, indent=4)


def add_employee(employee):
    employees = load_employee_data()
    employees.append(employee)
    save_employee_data(employees)


def update_employee(employee_id, updated_info):
    employees = load_employee_data()
    for employee in employees:
        if employee['id'] == employee_id:
            employee.update(updated_info)
            save_employee_data(employees)
            return
    print(f"Employee with ID {employee_id} not found.")


def delete_employee(employee_id):
    employees = load_employee_data()
    employees = [emp for emp in employees if emp['id'] != employee_id]
    save_employee_data(employees)


def get_employee(employee_id):
    employees = load_employee_data()
    for employee in employees:
        if employee['id'] == employee_id:
            return employee
    print(f"Employee with ID {employee_id} not found.")
    return None


# Example usage:
if __name__ == "__main__":
    # Adding employees
    add_employee({"id": 1, "name": "John Doe", "position": "Developer", "salary": 60000})
    add_employee({"id": 2, "name": "Jane Smith", "position": "Manager", "salary": 80000})

    # Updating an employee
    update_employee(1, {"name": "Johnathan Doe", "salary": 65000})

    # Deleting an employee
    delete_employee(2)

    # Retrieving an employee
    employee = get_employee(1)
    if employee:
        print(employee)
