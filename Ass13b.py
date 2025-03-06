class MethodOverloadingExample:

    # Method with one integer parameter
    def print_info(self, num):
        if isinstance(num, int):
            print(f"Integer: {num}")
        else:
            print("Invalid argument. Expected an integer.")

    # Method with one string parameter
    def print_info(self, text):
        if isinstance(text, str):
            print(f"String: {text}")
        else:
            print("Invalid argument. Expected a string.")

# Create an object
obj = MethodOverloadingExample()

# Call method with an integer argument
obj.print_info(10)

# Call method with a string argument
obj.print_info("Hello, Python")
