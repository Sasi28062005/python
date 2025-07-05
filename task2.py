#Write a basic program to input a user's name and greet them
a= input("Please enter your name: ");
print("Hello, " + a + "! Welcome to the program.");
#Convert temperature from Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "));
fahrenheit = (celsius * 9/5) + 32;
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.");
#Find the largest of three numbers.
num1 = float(input("Enter first number: "));
num2 = float(input("Enter second number: "));
num3 = float(input("Enter third number: "));
largest = max(num1, num2, num3);
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.");
#Check whether a number is positive, negative, or zero.
number = float(input("Enter a number: "));
if number > 0:
    print(f"{number} is a positive number.");
elif number < 0:
    print(f"{number} is a negative number.");
else:
    print("The number is zero.");
#Check if a character is a vowel or consonant.
char = input("Enter a character: ").lower();
if char in 'aeiou':
    print(f"{char} is a vowel.");
else:
    print(f"{char} is a consonant.");
#Sum all numbers from 1 to n.
n = int(input("Enter a positive integer n: "));
sum_n = sum(range(1, n + 1));
print(f"The sum of all numbers from 1 to {n} is {sum_n}.");
#Check if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number to check if it is prime: "));
if is_prime(number):
    print(f"{number} is a prime number.");
else:
    print(f"{number} is not a prime number.");
#Find the length of a string without using len().
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
string = input("Enter a string: ");
length = string_length(string);
print(f"The length of the string '{string}' is {length} characters.");
#Replace all spaces in a string with underscores.
def replace_spaces_with_underscores(s):
    return s.replace(' ', '_')
string = input("Enter a string: ");
modified_string = replace_spaces_with_underscores(string);
print(f"The modified string is: '{modified_string}'");
#Create a list and print all its elements.
def print_list_elements(lst):
    for index, element in enumerate(lst):
        print(f"Element at index {index}: {element}")
lst = input("Enter a list of elements separated by commas: ").split(',');
print_list_elements(lst)
#Find the largest number in a list.
def find_largest_in_list(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
lst = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
largest = find_largest_in_list(lst)
print(f"The largest number in the list is: {largest}")
#Write a function to find the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number to find its factorial: "))
fact = factorial(n)
print(f"The factorial of {n} is {fact}.")
#Create a class Car with attributes brand and model, and create an object of it.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
brand = input("Enter car brand: ")
model = input("Enter car model: ")
car = Car(brand, model)
car.display_info()
#Write a class Person with a method to display their name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
person = Person(name, age)
person.display_info()
#Write a class Book with a constructor to initialize title and author.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")
title = input("Enter book title: ")
author = input("Enter book author: ")
book = Book(title, author)
book.display_info()
#Create a class Employee with a constructor that initializes name and salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")
name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
employee = Employee(name, salary)
employee.display_info()
#Create a base class Animal and a derived class Dog that inherits from it.
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print(f"The {self.species} makes a sound.")
class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def bark(self):
        print(f"{self.name} barks.")
name = input("Enter dog's name: ")
dog = Dog(name)
dog.make_sound()
dog.bark()
#Create a base class Vehicle, and classes Car and Bike that inherit from it.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}")
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

    def display_info(self):
        print(f"Bike Brand: {self.brand}, Type: {self.type}")
brand = input("Enter vehicle brand: ")
vehicle_type = input("Enter vehicle type (Car/Bike): ").lower()
if vehicle_type == 'car':
    model = input("Enter car model: ")
    vehicle = Car(brand, model)
elif vehicle_type == 'bike':
    type = input("Enter bike type: ")
    vehicle = Bike(brand, type)
else:
    print("Invalid vehicle type.")
    vehicle = None
if vehicle:
    vehicle.display_info()
    
