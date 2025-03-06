# Part 1: Define a custom exception
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)  # Pass the message to the base Exception class

# Part 2: Method that raises a custom exception
def check_value(value):
    print(f"Checking value: {value}")
    if value < 0:
        # Raise the custom exception when the value is negative
        raise MyCustomException("Negative value is not allowed!")
    else:
        print("Value is valid.")

# Part 3: Main function with try-except-finally block
def main():
    try:
        # Test with a negative value to trigger the custom exception
        check_value(-5)
    except MyCustomException as e:
        # Handle the custom exception
        print(f"Caught an exception: {e}")
    finally:
        # This block is always executed, no matter what
        print("Finally block executed. Cleanup can be done here.")

    try:
        # Test with a positive value
        check_value(10)
    except MyCustomException as e:
        # Handle the custom exception (though it won't be raised here)
        print(f"Caught an exception: {e}")
    finally:
        # This block is always executed
        print("Finally block executed after second call.")

# Call the main function to run the program
main()
