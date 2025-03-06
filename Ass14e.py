def multiple_except_blocks():
    try:
        # Simulating a ValueError
        num = int("hello")  # This will raise ValueError because "hello" can't be converted to an integer

        # Simulating a ZeroDivisionError
        result = 10 / 0  # This will raise ZeroDivisionError

    except ValueError as e:
        print("Caught a ValueError: Invalid value entered!")
        print(f"Error details: {e}")

    except ZeroDivisionError as e:
        print("Caught a ZeroDivisionError: Division by zero!")
        print(f"Error details: {e}")

    except Exception as e:  # This will catch any other exception that is not specifically handled above
        print("Caught an unexpected exception!")
        print(f"Error details: {e}")

# Calling the function to demonstrate the multiple catch blocks
multiple_except_blocks()
