# file_handling_assignment.py

def create_and_write_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line.\n")
            file.write("12345 is a number.\n")
            file.write("This is the third line.\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    finally:
        print("Exiting write operation.\n")

def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("Exiting read operation.\n")

def append_to_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending the fourth line.\n")
            file.write("67890 is another number.\n")
            file.write("Appending the sixth line.\n")
        print("File appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("Exiting append operation.\n")

def main():
    create_and_write_file()
    read_file()
    append_to_file()
    read_file()  

if __name__ == "__main__":
    main()
