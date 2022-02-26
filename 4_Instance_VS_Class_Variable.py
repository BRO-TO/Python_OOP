class User:
    total = 0

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        User.total += 1

# Broto, Fajar
# name, email, role

Broto = User("BROT", "BROT@gmail.com", "user")
print(User.total)

Fajar = User("FAJ", "FAJ@gmail.com", "admin")
print(User.total)

# Broto.name = "Brot"
# Fajar.name = "Faj"

print(Broto.name)
print(Broto.email)
print(Broto.role)