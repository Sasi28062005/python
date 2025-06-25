#create a list of 5 numbers.print the sum and average
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
sum_of_numbers = sum(numbers)
average_of_numbers = sum_of_numbers / len(numbers)
print(f"The sum of the numbers is: {sum_of_numbers}")
print(f"The average of the numbers is: {average_of_numbers}")
#Store 5 subjects and marks in a dictionary. Display subject with the highest marks.
subjects = {}
for i in range(5):
    subject = input(f"Enter subject {i + 1}: ")
    marks = int(input(f"Enter marks for {subject}: "))
    subjects[subject] = marks
highest_subject = max(subjects, key=subjects.get)
highest_marks = subjects[highest_subject]
print(f"The subject with the highest marks is: {highest_subject} with {highest_marks} marks")
#create a tuple of 5 elements. print it in reverse order
elements = []
for i in range(5):
    element = input(f"Enter element {i + 1}: ")
    elements.append(element)        
elements_tuple = tuple(elements)
reversed_tuple = elements_tuple[::-1]
print(f"The tuple in reverse order is: {reversed_tuple}")
#Write a program to count the number of vowels in a string.
string_input = input("Enter a string to count the number of vowels: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in string_input if char in vowels)
print(f"The number of vowels in the string is: {count}")