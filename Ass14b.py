# Program to handle ArithmeticException using try-catch block
def handle_arithmetic_exception():
    try:
        # This will cause an ArithmeticError (ZeroDivisionError in Python)
        result = 10 / 0  # Division by zero
        print(result)
    except ZeroDivisionError as e:
        print("Handled Exception: Cannot divide by zero!")
        print(f"Error Details: {e}")

# Call the function to handle the exception
handle_arithmetic_exception()
