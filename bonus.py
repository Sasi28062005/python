#Create a simple student mark calculator using functions and dictionaries. Input name and 3 subject marks, and print total, average, and grade
marks= {}
def calculate_total_and_average(marks):
    total = sum(marks.values())
    average = total / len(marks)
    return total, average
def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
def student_mark_calculator():
    name = input("Enter the student's name: ")
    subjects = ['Math', 'Science', 'English']
    
    for subject in subjects:
        marks[subject] = float(input(f"Enter marks for {subject}: "))
    
    total, average = calculate_total_and_average(marks)
    grade = determine_grade(average)
    
    print(f"\nStudent Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
if __name__ == "__main__":
    student_mark_calculator()
