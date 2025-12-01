
from employe import get_employee_info

def test_get_employee_info():
   
    name = "John Doe"
    emp_id = "E123"
    department = "IT"
    salary = 50000

    
    expected_output = (
        "Employee Name: John Doe\n"
        "Employee ID: E123\n"
        "Department: IT\n"
        "Salary: 50000"
    )

    
    assert get_employee_info(name, emp_id, department, salary) == expected_output
