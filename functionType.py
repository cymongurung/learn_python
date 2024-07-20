# # write a program to print even numbers between start to end using function

# def print_even(start, end):
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num)

# start = 100
# end = 150

# print_even(start, end)
# #  Types of Function 
# # system Define
# #  User Define


# # 1.No paramater & No Return Type
# #  2.Parameter  & No Return type
# #  3.Parameter & Return Type 
# #  4.No Parameter & Return type

# # 1.No paramater & No Return Type
# # if there is nothing inside the bracket it is called no parameter
# # if there is no return keyword, it means function do not return any values.
# def display_details():
#     print("My name is Suman")
#     print("I am from Pokhara")

# display_details()

#  2.Parameter  & No Return type
def add(n1 , n2):
    total = n1 + n2
    print(f"The total is {total }")

add(50,40)  


# #  3.Parameter & Return Type 
# def find_cube(number):
#     cube = number * number * number
#     return cube

# myValue = find_cube(2)
# print(myValue)


# #  4.No Parameter & Return type
def minvoter_age():
    return 18
print (minvoter_age())


ram_age = 23

if ram_age >= minvoter_age():
    print("You are a voter")