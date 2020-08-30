# object-oriented programming

class Employee:
    def __init__(self, first, last, pay):  # constructor in some other languages
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    # instead of typing print('{} {}'.format(emp_1.first, emp_1.last))
    # put self to prevent TypeError that says it takes 0 positional args but 1 is given
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
# self is instance

# instances
emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#  emp_1 passed in self, corey = first, shafer = last, pay = 50000


print("1")
print(emp_1.fullname())  # need parenthesis because it is a method
#  without the parenthesis, it is an attribute
# w/o () , it will print the method instead of the return value of the method

# we can run this w/class name itself
print("2")
print(emp_1.fullname())
print("3")
print(Employee.fullname(emp_1))
# they do the exact same thing



print('-' * 10)
print("4")
print(emp_1)
print("5")
print(emp_2)
print("6")
print(emp_1.email)
print("7")
print(emp_2.email)

# emp_1.first = "Corey"
# emp_1.last = "Shafer"
# emp_1.email = "corey.shafer@company.com"
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = "test.user@company.com"
# emp_2.pay = 60000

