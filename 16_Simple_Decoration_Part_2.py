def info(func):
    def wrapper():
        print("*" * 10)
        func()
        print("#" * 10)

    return wrapper
        

print("")

@info
def say_hello():
    print("Hello World Of Python")



say_hello()
