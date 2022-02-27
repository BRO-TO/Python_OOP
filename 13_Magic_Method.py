# magic method yg pakai underscore 2 kali (__)

class Game:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        print("aku dipanggil lho")

    def __str__(self):
        return f"{self.title} - ${self.price}"

    def __eq__(self, other):
        return self.title == other.title

    def __gt__(self, other):
        return self.price > other.price

    def __add__(self, other):
        return self.price + other.price

zelda = Game("Breath of the wild", 69)
zelda2 = Game("Breath of the wild", 60)
mario = Game("Paper Mario Origami King", 65)

print("")
print(zelda + zelda2)