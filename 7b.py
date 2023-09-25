class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Salary: ₹{self.salary:.2f}")

    def update_salary(self, new_salary):
        self.salary = new_salary

employee1 = Employee("Rajesh Kumar", 101, "HR", 50000.0)
employee2 = Employee("Priya Sharma", 102, "Engineering", 60000.0)
employee3 = Employee("Amit Patel", 103, "HR", 55000.0)


print("Employee Details:")
print("-------------------------------")
employee1.display_details()
print("-------------------------------")
employee2.display_details()
print("-------------------------------")
employee3.display_details()
print("-------------------------------")

hr_new_salary = 52000.0
employee1.update_salary(hr_new_salary)
employee3.update_salary(hr_new_salary)

print("\nEmployee Details after Salary Update (HR Department):")
print("-------------------------------")
employee1.display_details()
print("-------------------------------")
employee3.display_details()
print("-------------------------------")
