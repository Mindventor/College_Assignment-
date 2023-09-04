class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_employees(employees, key):
    if key == 1:
        return sorted(employees, key=lambda x: x.age)
    elif key == 2:
        return sorted(employees, key=lambda x: x.name)
    elif key == 3:
        return sorted(employees, key=lambda x: x.salary)
    else:
        return employees

def print_employees(employees):
    for employee in employees:
        print(f"Employee ID: {employee.employee_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

if __name__ == "__main__":
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    while True:
        print("\nChoose sorting parameter:")
        print("1. Age")
        print("2. Name")
        print("3. Salary")
        print("4. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 4:
            break
        
        employees = sort_employees(employees, choice)
        print("\nSorted Employee Table:")
        print_employees(employees)
