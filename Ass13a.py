class MethodOverloadingExample:

    # Method with one parameter
    def print_message(self, msg):
        print(f"Message: {msg}")

    # Method with two parameters
    def print_message(self, msg1, msg2=None):
        if msg2:
            print(f"Message 1: {msg1} | Message 2: {msg2}")
        else:
            print(f"Message: {msg1}")

# Create an object
obj = MethodOverloadingExample()

# Call method with one argument
obj.print_message("Hello, World!")

# Call method with two arguments
obj.print_message("Hello", "Python")
