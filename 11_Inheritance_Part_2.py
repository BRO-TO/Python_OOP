# inheritance, extend, override, polymorphism
class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def work(self):
        return f"{self.name} is working"

class Programmer(Employee):
    def __init__(self, name, email, level):
        super().__init__(name, email)
        self.level = level

    # Extend
    def debug(self):
        return "debugging"

    def work(self):
        return f"{self.name} is writing code"

class UIDesigner(Employee):
    def __init__(self, name, email, level, tools):
        super().__init__(name, email)
        self.level = level
        self.tools = tools

    def work(self):
        return f"{self.name} is designing some new cool product"

print("")

employee = Employee("broto", "broto@company.com")
print(employee.work())
# print(employee.debug())

programmer = Programmer("FS", "FS@ssj.com", "senior")
print(programmer.work())
print(programmer.debug())
print(programmer.level)
print(programmer.name)

ui_designer = UIDesigner("Bambang", "bambang@zizazu.com", "senior", "visual studio code")
print(ui_designer.work())