# 1. Write a program to generate ArithmeticException without exception handling
def generate_arithmetic_exception():
    num = 10 / 0  # Division by zero will raise ArithmeticError (equivalent to ArithmeticException in other languages)


# 2. Handle the ArithmeticException using try-catch block
def handle_arithmetic_exception():
    try:
        num = 10 / 0  # Division by zero
    except ArithmeticError as e:
        print("Handled ArithmeticError: Division by zero occurred!")

# 3. Write a method which throws exception, Call that method in main class without try block
def method_that_throws_exception():
    raise Exception("This is a custom exception from method.")


# 4. Write a program with multiple catch blocks
def multiple_catch_blocks():
    try:
        num = int("a")  # Will raise ValueError
        num = 10 / 0  # Will raise ArithmeticError
    except ValueError as e:
        print("Handled ValueError: Invalid value entered.")
    except ArithmeticError as e:
        print("Handled ArithmeticError: Division by zero occurred!")

# 5. Write a program to throw exception with your own message
def throw_exception_with_message():
    raise Exception("Custom exception with a message")


# 6. Write a program to create your own exception
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def raise_custom_exception():
    raise CustomException("This is my custom exception!")


# 7. Write a program with finally block
def finally_block_example():
    try:
        print("Trying to open a file.")
        num = 10 / 0  # This will cause an ArithmeticError
    except ArithmeticError as e:
        print("Caught an arithmetic error!")
    finally:
        print("This is the finally block, and it always executes!")


# 8. Write a program to generate ArithmeticException
def generate_arithmetic_exception():
    return 10 / 0  # This will cause ArithmeticError


# 9. Write a program to generate FileNotFoundException
def generate_file_not_found_exception():
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print("Handled FileNotFoundError: The file could not be found.")


# 10. Write a program to generate ClassNotFoundException
def generate_class_not_found_exception():
    try:
        # This would typically be used with dynamic imports, so here we'll simulate it:
        __import__("non_existent_module")  # This will raise an ImportError, simulating ClassNotFoundException
    except ImportError as e:
        print("Handled ImportError (similar to ClassNotFoundException): The class/module could not be found.")


# 11. Write a program to generate IOException
def generate_io_exception():
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except IOError as e:  # In Python, IOError includes cases like file not found
        print("Handled IOError: Input/Output operation failed.")


# 12. Write a program to generate NoSuchFieldException
class NoSuchFieldExceptionExample:
    def __init__(self):
        self.field = "I exist!"
    
    def check_field(self):
        try:
            print(self.non_existent_field)  # This will raise an AttributeError
        except AttributeError as e:
            print("Handled AttributeError (similar to NoSuchFieldException): Field does not exist.")

