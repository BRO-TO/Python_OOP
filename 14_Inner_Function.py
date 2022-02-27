class Game:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        print("aku dipanggil lho")

    """ def info(self):
        def print_title():
            return f"Title : {self.title}"

        def print_price():
            return f"Price : {self.price}"

        print_title()
        print_price() """

    def info(self):
        def print_title():
            return f"Title : {self.title}"

        def print_price():
            return f"Price : {self.price}"

        return print_title
        

print("")

zelda = Game("Breath of the wild", 69)
title = zelda.info()

print(title)
print(title())
