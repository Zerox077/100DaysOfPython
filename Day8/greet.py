def greet():
    print("Hello")
    print("How are you ?")
    print("How is the weather")

greet()

def greet_with_name(name):
    print(f"Hello {name}")


greet_with_name("Amit")


# Functions with more than 1 input
def greet_with_name_location(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with_name_location(name="Amit", location="India")


