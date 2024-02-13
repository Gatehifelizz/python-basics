num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")
age = int(input("Enter your age: "))
name = input("Enter your name: ")
if age >= 18:
    print(f" hello {name} you are eligible to vote, proceed!")

else:
    print(f"Hello {name} you are not eligible to vote, cannot proceed!")

# elif statements
marks=int(input("enter marks:"))

if marks>=80 and marks<=100:
    print("you have an A")
elif marks >=60and marks<=79:
    print("you have a B")
elif marks>=40 and marks<=59:
    print("you have an C")
elif marks>=0 and marks<=39:
    print("you have terriblyfalied")
else:
    print("Wrong input please try again")




