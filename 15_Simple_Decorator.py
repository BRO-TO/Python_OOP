""" class Game:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        print("aku dipanggil lho") 

     def info(self):
        def print_title():
            return f"Title : {self.title}"

        def print_price():
            return f"Price : {self.price}"

        print_title()
        print_price() """

""" def info(self):
    def print_title():
        return f"Title : {self.title}"

    def print_price():
        return f"Price : {self.price}"

    return print_title """

def info(func):
    def wrapper():
        print("*" * 10)
        func()
        print("#" * 10)

    return wrapper
        

print("")

def say_hello():
    print("Hello World Of Python")

say_hello = info(say_hello)

say_hello()

