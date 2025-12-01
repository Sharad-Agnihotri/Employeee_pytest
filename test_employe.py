
from employe import employee_info

def test_employee_info():
   
    expected_output = (
        "Employee Name: John Doe\n"
        "Employee ID: E123\n"
        "Department: IT\n"
        "Salary: 50000"
    )

    
    assert employee_info("Alice", "E101", "IT", 55000) == expected_output
