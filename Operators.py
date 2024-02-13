# arithmetic operator
num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)

# comparison operator
num3 = int(input("Enter num 3:"))
num4 = int(input("Enter num 4:"))
print(f"{num3}is equal to {num4}: {num3 == num4} ")
print(f"{num3}is not equal to {num4}: {num3 != num4} ")
print(f"{num3}is greater than {num4}: {num3 >= num4} ")
print(f"{num3}is less than {num4}: {num3 < num4} ")

num5 = int(input("enter number"))
print(f"both statements should be true {num5==9 and num5>15}")
print(f"one statements should be true {num5==9 or num5>15}")
