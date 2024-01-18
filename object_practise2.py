class  Employee:
    def __init__(emp,emp_name,emp_ID,emp_salary,emp_department):
        emp.name = emp_name
        emp.ID = emp_ID
        emp.salary = emp_salary
        emp.department = emp_department

    def assign_department(emp,emp_department):
        emp.department = emp_department
        emp.department.append(input("Change Department"))
    
    def print_employee_details(emp):
        print(f"The employee {emp.name},ID number{emp.ID},is in {emp.department} and earns {emp.salary}")

    def calculate_emp_salary(salary,hours_worked):
        salary = input("What is the standard salary of this employee")
        hours_worked = input("How many hours did they work")
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (salary / 50))
            salary = salary + overtime_amount

    
