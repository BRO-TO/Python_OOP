class User:
    total = 0

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.__role = role
        User.total += 1

    def info(self):
        return f"{self.name} - {self.email} - {self.__role}"

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, new_role):
        if self.__role != "user":
            self.__role = new_role

    

broto = User("BROTOFS", "broto@gmail.com", "user")

print(broto.info())
broto.role = "super_admin"
print(broto.info())