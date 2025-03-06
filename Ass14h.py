# 1. Simulate FileNotFoundException (FileNotFoundError in Python)
def file_not_found_example():
    try:
        # Attempt to open a file that doesn't exist
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Caught an exception: FileNotFoundError - {e}")

# 2. Simulate ClassNotFoundException (ImportError in Python)
def class_not_found_example():
    try:
        # Try importing a non-existing module
        import non_existent_module # type: ignore
    except ImportError as e:
        print(f"Caught an exception: ImportError - {e}")

# 3. Simulate IOException (OSError in Python)
def io_exception_example():
    try:
        # Simulate an IO operation error (attempting to write to a read-only file system)
        raise OSError("Simulated I/O exception.")
    except OSError as e:
        print(f"Caught an exception: OSError - {e}")

# 4. Simulate NoSuchFieldException (AttributeError in Python)
class MyClass:
    def __init__(self):
        self.my_attribute = "I exist!"

def no_such_field_example():
    try:
        # Try to access a non-existing attribute (NoSuchFieldException equivalent)
        obj = MyClass()
        print(obj.non_existent_attribute)  # This will raise an AttributeError
    except AttributeError as e:
        print(f"Caught an exception: AttributeError - {e}")

# Main function to demonstrate each exception
def main():
    print("1. FileNotFoundException (FileNotFoundError in Python):")
    file_not_found_example()
    
    print("\n2. ClassNotFoundException (ImportError in Python):")
    class_not_found_example()
    
    print("\n3. IOException (OSError in Python):")
    io_exception_example()
    
    print("\n4. NoSuchFieldException (AttributeError in Python):")
    no_such_field_example()

# Run the main function
if __name__ == "__main__":
    main()
