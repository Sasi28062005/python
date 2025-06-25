#Write a program to create a text file and write 5 lines into it.

def create_and_write_file(filename):
    try:
        with open(filename, 'w') as file:
            for i in range(5):
                line = input(f"Enter line {i + 1} to write into the file: ")
                file.write(line + '\n')
        print(f"Successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
def append_to_file(filename):
    try:
        with open(filename, 'a') as file:
            line = input("Enter a line to append to the file: ")
            file.write(line + '\n')
        print(f"Successfully appended to {filename}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
def delete_file(filename):
    import os
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Successfully deleted {filename}")
        else:
            print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")
def file_operations():
    filename = input("Enter the filename to perform operations on: ")
    while True:
        print("\nFile Operations Menu:")
        print("1. Create and write to file")
        print("2. Read file")
        print("3. Append to file")
        print("4. Delete file")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            create_and_write_file(filename)
        elif choice == '2':
            read_file(filename)
        elif choice == '3':
            append_to_file(filename)
        elif choice == '4':
            delete_file(filename)
        elif choice == '5':
            print("Exiting file operations.")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    file_operations()
