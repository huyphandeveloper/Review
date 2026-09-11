from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name, salary):
        self.__id = id
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = amount

    @abstractmethod
    def calculate_salary(self):
        pass

# decorate bổ sung log hiển thị sau khi tính lương.
def log_salary_calculation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        tmp = args[0]
        print(f"[LOG] Calculating salary for {tmp.name}: {result}")

        return result
    return wrapper

class Developer(Employee):
    @log_salary_calculation
    def calculate_salary(self, bonus):
        sum_salary = self.salary + 1000 * bonus
        return sum_salary

class Salesperson(Employee):
    @log_salary_calculation
    def calculate_salary(self, sales_commission):
        sum_salary = self.salary + 250 * sales_commission
        return sum_salary

list_employee = [Developer(1, "Kien", 3000), Salesperson(2, "Thuy", 2000)]

for employee in list_employee:
    print(employee.calculate_salary(5))
