class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def sort_employees(self, sort_key):
        if sort_key == 1:  # Sort by Age
            self.employees.sort(key=lambda emp: emp.age)
        elif sort_key == 2:  # Sort by Name
            self.employees.sort(key=lambda emp: emp.name)
        elif sort_key == 3:  # Sort by Salary
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter")

    def print_table(self):
        print("Employee ID  |  Name       |  Age |  Salary (PM)")
        print("-" * 45)
        for emp in self.employees:
            print(f"{emp.emp_id}      |  {emp.name:10} |  {emp.age}   |  {emp.salary}")

def main():
    emp_table = EmployeeTable()

    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    sort_choice = int(input("Enter your choice: "))

    emp_table.sort_employees(sort_choice)
    emp_table.print_table()

if __name__ == "__main__":
    main()
