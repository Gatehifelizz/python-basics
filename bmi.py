# BMI FUNCTION
weight = float(input("enter your weight in Kg:"))
height = float(input("enter your height in meters"))
name = input("enter your name: ")
bmi=weight/(height**2)
if bmi < 18.5:
    print("you are underweight")
elif bmi>=18.6 and bmi<=24.9:
    print(f"hello {name} you are healthy")
elif bmi>=25.0 and bmi<=29.9:
    print(f"hello {name }you are overweight ")
elif bmi>30.0:
    print(f"hello {name} you are Obese")
else:
    print("Wrong value! please try again")


