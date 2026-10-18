def add_sprinkles(func):
    def wrapper():
        print("you add sprinkles 🎊")
        func()
    return wrapper   # <-- aligned properly


@add_sprinkles
def get_ice_cream():
    print("Here is your ice cream 🍨")

get_ice_cream()
