#print all even numbers from 1 to 100
num1= 1
while num1 <= 50:
    if num1 % 2 == 0:
        print(num1, end=' ');
    num1 += 1;

# display the multiplication table of a number
num = int(input("\nEnter a number to display its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")  ;

# program to find the sum of digits of a number.
num = int(input("\nEnter a number to find the sum of its digits: "))
sum_of_digits = 0;
while num > 0:
    digit = num % 10;
    sum_of_digits += digit;
    num //= 10;
print(f"The sum of the digits is: {sum_of_digits}");
# program to check if a number is prime
num = int(input("\nEnter a number to check if it is prime: ")) ;
is_prime = True;
if num <= 1:
    is_prime = False;
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False;
        break;
if is_prime:
    print(f"{num} is a prime number.");
else:
    print(f"{num} is not a prime number.");
# program to reverse a string
num1 = input("\nEnter a string to reverse it: ");
reversed_string = num1[::-1];
print(f"The reversed string is: {reversed_string}");    

