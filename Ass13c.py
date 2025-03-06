class MethodOverloadingExample:

    # Method with one parameter, default behavior
    def print_details(self, info):
        print(f"Information: {info}")

    # Method with same number of parameters and same type (overrides the first method)
    def print_details(self, info):
        print(f"Details: {info}")

# Create an object
obj = MethodOverloadingExample()

# Call method with a single argument
obj.print_details("Some details about Python.")
