# Design HR system
# implement payroll system for different employees
# class provides a class method which takes a list of employees and displays their name and calculates their payroll
from abc import abstractmethod


class Employee:
    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary

    @property
    def email(self):
        return self.name + '.' + self.lastname + '@companymail.com'

    @property
    def fullname(self):
        return self.name + ' ' + self.lastname

    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.name = fname
        self.lastname = lname

    def __str__(self):
        return "First Name:{}, Last Name = {}, Salary = {}".format(self.name, self.lastname, self.salary)

    @abstractmethod
    def calculate_payroll(self):
        pass


class Manager(Employee):

    def __init__(self, name, lastname, salary, team_members=None):
        super().__init__(name, lastname, salary)

        if team_members is not None:
            self.team_members = team_members
            self.__team_size = len(self.team_members)
        else:
            self.team_members = []
            self.__team_size = 0

    def calculate_payroll(self):
        return (self.salary * 0.10) + self.salary

    def add_team_members(self, employee):
        self.team_members.append(employee)
        self.__team_size += 1

    @property
    def team_size(self):
        return self.__team_size

    def make_budget(self):
        return self.__team_size * 1000


class Developer(Employee):

    def __init__(self, name, lastname, salary, prog_lang='C'):
        super().__init__(name, lastname, salary)
        self.prog_lang = prog_lang

    def calculate_payroll(self):
        return (self.salary * 0.20) + self.salary


class EmployeePayroll:
    def calculate_payroll(self, lemployees=None):
        if lemployees is not None:
            for employee in lemployees:
                print("Fullname:" + employee.fullname)
                print("Email:" + employee.email)
                print("Bonused Salary:" + str(employee.calculate_payroll()))


if __name__ == '__main__':
    emp1 = Developer('Suman', 'Bidarahalli', 85000, 'Python')
    print(emp1)
    print(emp1.email)
    print(emp1.fullname)
    emp2 = Developer('Ivo', 'Bidarahalli', 87000, 'JS')
    print(emp2)
    print(emp2.email)
    print(emp2.fullname)
    emp3 = Developer('Ivo', 'Ernst', 87000, 'Java')
    print(emp3)
    print(emp3.email)
    print(emp3.fullname)
    manager_1 = Manager('Stefan', 'Erras', 125000, [emp1, emp2])
    manager_2 = Manager('Mark', 'Mamut', 115000, [emp3])
    print(manager_1)
    print(manager_1.email)
    print(manager_1.fullname)
    print(manager_1.team_size)
    print(manager_2)
    print(manager_2.email)
    print(manager_2.fullname)
    print(manager_2.team_size)
    emp4 = Developer('Rebecca', 'Taylor', 81000, 'R')
    print(emp4)
    print(emp4.email)
    print(emp4.fullname)
    manager_2.add_team_members(emp4)
    print(manager_2.team_size)
    ep = EmployeePayroll()
    ep.calculate_payroll([emp1, emp2, emp3, manager_1, manager_2])
    print(type(Employee))
    print(type(emp1))
    print(emp1.__class__)
    print(isinstance(emp1, Developer))
    print(isinstance(Developer, type))
    print(issubclass(Developer, object))
    print(issubclass(Developer, Employee))

    print(Developer.__bases__)
    print(Employee.__bases__)
