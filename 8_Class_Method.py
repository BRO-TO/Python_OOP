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

    @classmethod
    def setTotal(cls, total):
        cls.total = total

    @classmethod
    def from_string(cls, string_param):
        name, email, role = string_param.split("-")
        return cls(name , email, role)
    
broto = User("BROTOFS", "broto@gmail.com", "user")
string_params = "Zelda-zelda@nintendo.com-admin"

zelda_dua = User.from_string(string_params)

print("")
print(zelda_dua.info())

# print(broto.info())
# broto.role = "super_admin"
# print(broto.info())