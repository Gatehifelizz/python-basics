students = ["martin", "james", "michael", "jessica", "michael", "james", "evans"]
for _ in students:
    print(_)
mystring = "Gatehi Nyoike"
for _ in mystring:
    print(_)

    # exercise
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for i in num_list:
    total = total + i
    print(f" sum is :{total}")
# even check function
my_list = ["kenya", "james", "michael", "evans", "wanjohi"]
x = len(my_list[2])
print(x)


# even check
def my_function(country="Kenya"):
    print("I come from" + country)

    my_function("Rwanda")
    my_function("Niger")
    my_function()
    my_function("Zambia")

    my_function(country)