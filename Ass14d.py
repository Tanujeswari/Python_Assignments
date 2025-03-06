# Method that throws an exception
def method_that_throws_exception():
    # This will raise a custom exception
    raise Exception("This is a custom exception thrown from the method.")

# Main function where the exception is called without try-except
def main():
    print("Calling the method that throws an exception...")
    method_that_throws_exception()  # This will raise an exception

# Call the main function
main()
