# Functions

def function():  # function without argument and no return type
    print("Hello Vasanth")


function()


def function_with_args(a, b):  # function with argument and no return type
    div = a % b
    print(div)


function_with_args(10, 6)


def function_with_default(a=10, b=20):  # function with argument and no return type
    div = a % b
    print(div)


function_with_default()
function_with_default(10, 3)
function_with_default(a=10, b=4)


def function_with_return_type():  # return type without argument
    a, b = 10, 20
    sum1 = a + b
    return sum1


sum2 = function_with_return_type()
print(sum2)


def function_with_def_return(name, age):  # return with argument
    return name, age


user_details = function_with_def_return("vasanth", 24)
user_details2 = function_with_def_return("varun", 22)
print(user_details)
print(user_details2)


def function_with_def_return(a, b):
    concat = str(a) + b
    return concat


concat2 = function_with_def_return(10, 'savant')
print(concat2)
