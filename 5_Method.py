class User:
    total = 0

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        User.total += 1

    def info(self):
        return f"{self.name} - {self.email} - {self.role}"

    def update_role(self, new_role):
        if self.role != "user":
            self.role = new_role

# Broto, Fajar
# name, email, role

Broto = User("BROT", "BROT@gmail.com", "user")
# print(User.total)
print(Broto.info())

Broto.update_role("moderator")
print(Broto.info())

Fajar = User("FAJ", "FAJ@gmail.com", "admin")
# print(User.total)
print(Fajar.info())

Fajar.update_role("Super Admin")
print(Fajar.info())

# Broto.name = "Brot"
# Fajar.name = "Faj"

# print(Broto.name)
# print(Broto.email)
# print(Broto.role)

# print(User.name)

