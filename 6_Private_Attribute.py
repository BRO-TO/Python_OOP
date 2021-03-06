class User:
    total = 0

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.__role = role
        User.total += 1

    def info(self):
        return f"{self.name} - {self.email} - {self.__role}"

    def update_role(self, new_role):
        if self.__role != "user":
            self.__role = new_role

    def getRole(self):
        return self.__role

broto = User("BROTOFS", "broto@gmail.com", "user")
print(broto.__dict__)
print(broto._User__role)
print(broto.getRole())