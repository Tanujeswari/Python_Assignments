import os

# 1. Write a program to read a text file
def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

# 2. Write a program to write text to .txt file using InputStream
def write_text_file(file_name):
    print(f"Enter text to write to {file_name}. Type 'exit' to finish.")
    try:
        with open(file_name, 'w') as file:
            while True:
                text = input()
                if text.lower() == 'exit':
                    break
                file.write(text + '\n')
            print(f"Text has been written to {file_name}.")
    except Exception as e:
        print(f"Error: {e}")

# 3. Write a program to read a file stream
def read_file_stream(file_name):
    try:
        with open(file_name, 'rb') as file:
            content = file.read()
            print(f"File Content as stream (binary):\n{content}")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

# 4. Write a program to read a file stream supports random access
def read_file_random_access(file_name):
    try:
        with open(file_name, 'rb') as file:
            print("Reading the first 10 bytes of the file (random access):")
            print(file.read(10))  # Read first 10 bytes
            file.seek(0)  # Move pointer back to the beginning
            print("Reading first 10 bytes again (random access):")
            print(file.read(10))
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

# 5. Write a program to read a file and adjust to a particular index using seek()
def read_file_seek(file_name):
    try:
        with open(file_name, 'rb') as file:
            file.seek(5)  # Move to the 5th byte of the file
            print(f"Reading from byte index 5: {file.read(5)}")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

# 6. Write a program to check whether a file has read and write access permissions
def check_file_permissions(file_name):
    if os.access(file_name, os.R_OK):
        print(f"The file {file_name} has read access.")
    else:
        print(f"The file {file_name} does not have read access.")
    
    if os.access(file_name, os.W_OK):
        print(f"The file {file_name} has write access.")
    else:
        print(f"The file {file_name} does not have write access.")

def main():
    file_name = "example.txt"  # You can modify this to point to any text file on your system

    # Test reading a text file
    read_text_file(file_name)

    # Test writing text to a .txt file using InputStream (simulating this with standard input)
    write_text_file(file_name)

    # Test reading file stream (binary stream)
    read_file_stream(file_name)

    # Test random access read (reading specific bytes)
    read_file_random_access(file_name)

    # Test reading file and adjusting to a particular index using seek()
    read_file_seek(file_name)

    # Test checking read and write permissions
    check_file_permissions(file_name)

if __name__ == "__main__":
    main()
