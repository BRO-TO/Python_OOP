class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

# Broto, Fajar
# name, email, role

Broto = User("BROT", "BROT@gmail.com", "user")
Fajar = User("FAJ", "FAJ@gmail.com", "admin")

Broto.name = "Brot"
Fajar.name = "Faj"

print(Broto.name)
print(Broto.email)
print(Broto.role)