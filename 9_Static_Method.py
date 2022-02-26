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

    @staticmethod
    def tweet(word):
        return (word)
    
# broto = User("BROTOFS", "broto@gmail.com", "user")
tweet = User.tweet("Halo sedang belajar")
print("")
print(tweet)
