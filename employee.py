
def employee_info(name, emp_id, department, salary):
    result= (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
    return result

if __name__ == "__main__":
        name = "Alice\n"
        emp_id = "E101\n"
        department = "IT\n"
        salary = 55000

        print(employee_info(name, emp_id, department, salary))
