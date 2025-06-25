#Write a function to find the square and cube of a number.
def find_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
#a function that returns the number of uppercase and lowercaseletters in a string.
    return square, cube
def count_case_letters(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count
#Write a program to check if a string is a palindrome using a function.
def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]
#Write a function to calculate the area of a rectangle.
def calculate_area_of_rectangle(length, width):
    return length * width
if __name__ == "__main__":
    # Example usage of find_square_and_cube
    number = int(input("Enter a number to find its square and cube: "))
    square, cube = find_square_and_cube(number)
    print(f"Square of {number} is {square} and cube is {cube}")

    # Example usage of count_case_letters
    string_input = input("Enter a string to count uppercase and lowercase letters: ")
    upper_count, lower_count = count_case_letters(string_input)
    print(f"Uppercase letters: {upper_count}, Lowercase letters: {lower_count}")

    # Example usage of is_palindrome
    palindrome_string = input("Enter a string to check if it is a palindrome: ")
    if is_palindrome(palindrome_string):
        print(f"{palindrome_string} is a palindrome.")
    else:
        print(f"{palindrome_string} is not a palindrome.")

    # Example usage of calculate_area_of_rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculate_area_of_rectangle(length, width)
    print(f"The area of the rectangle is {area}.")
#Write a function to find the maximum and minimum in a list of numbers.
def find_max_min(numbers):
    if not numbers:
        return None, None
    max_number = max(numbers)
    min_number = min(numbers)
    return max_number, min_number
# Example usage of find_max_min
if __name__ == "__main__":
    numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    max_number, min_number = find_max_min(numbers)
    if max_number is not None and min_number is not None:
        print(f"Maximum number: {max_number}, Minimum number: {min_number}")
    else:
        print("The list is empty.")
#Write a function to sort a list of numbers in ascending order.
def sort_numbers(numbers):
    return sorted(numbers)
# Example usage of sort_numbers
if __name__ == "__main__":
    numbers = [int(x) for x in input("Enter numbers separated by spaces to sort: ").split()]
    sorted_numbers = sort_numbers(numbers)
    print(f"Sorted numbers: {sorted_numbers}")
#Write a function to find the factorial of a number.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
