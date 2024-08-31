name = input('Enter your name:  ')

my_list = []
even_list = []
odd_list = []

num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))

sum = num1 + num2 + num3

my_list.append(num1)
my_list.append(num2)
my_list.append(num3)

print(f"Hello, {name}! Let's explore your favorite numbers:")

for x in my_list:
    if  x % 2 == 0:
        print(f"{name} your number {x} is even")
        even_list.append(x)
    else:
        print(f"{name} your number {x} is odd")
        odd_list.append(x)

for x in my_list:
    sqr  = x ** 2
    print(f"The number {x} and its square: ({x}, {sqr})")


print(f"Amazing! The sum of your favorite numbers is: {sum}")

if sum % 2  == 1:
    result = f"Wow, {sum} is a prime number!"
else:
    result = f"{sum} is not a prime number, but it's still interesting!"
print(result)
print(f"Even numbers: {even_list}")