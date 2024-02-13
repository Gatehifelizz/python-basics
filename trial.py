def even_check(number):
    if number % 2 == 0:
        return True


x = even_check(20)
print(x)


# def check_even_list(num_list):
#   for number in num_list:
#         return True
#     else:
#        print(False)


# check_even_list([1, 5, ])

# base = int(input("Enter base length"))
# height = int(input("Enter height length"))

# print(f"the area of the triangle is {(0.5 * base * height)}")

# my_file.txt=("welcome to python programming language/n"
#            "this is the first line /n"
#           "this is the second straight line/n"
#          "this is the last line of code")


def financial_status_check(bank_balance):
    if bank_balance >= 2000:
        return "sufficient funds"
    elif bank_balance < 1000:
        return "insufficient funds"
    else:
        bank_balance > 1000
    return "financially stable"


bank_balance = int(input("Enter your bank balance: "))
financial_status_check(bank_balance)
print(financial_status_check(bank_balance))

my_string=("qwertyui")
print(my_string[0])


def lesser_of_two_evens(a,b):

