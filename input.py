name = input("Enter a name: ");
print("Hello,",name,"welcome to the program! ");

#add numbers
num1 = int(input("Enter first number: "));
num2 = int(input("Enter second number: "));
sum = num1 + num2;  
print("The sum of", num1, "and", num2, "is", sum);

#check if numvers are even or odd
if num1 % 2 == 0:
    print(num1, "is even"); 
else:
    print(num1, "is odd");
#find largest of three numbers
num1=int(input("Number1:"));
num2=int(input("Number2:"));
num3=int(input("Number3:"));
if num1 >= num2 and num1 >= num3:
    print(num1, "is the largest number");
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest number");       
else:
    print(num3, "is the largest number");
#calculate factorial
num1 = int(input("Enter a number to calculate its factorial: "));
factorial = 1;
for i in range(1, num1 + 1):
    factorial *= i;
print("The factorial of", num1, "is", factorial);
