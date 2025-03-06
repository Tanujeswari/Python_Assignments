# Program to generate an ArithmeticException without exception handling
def generate_arithmetic_exception():
    # This will cause an ArithmeticError (equivalent to ArithmeticException in Java)
    result = 10 / 0  # Division by zero will cause the exception
    print(result)

# Call the function to generate the exception
generate_arithmetic_exception()
