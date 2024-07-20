#create a function that reverse string
#for example Ram => Mar

# name = "Suman"
# print(name[4])
# print(name[3])
# print(name[2])
# print(name[1])
# print(name[0])


# name = "Suman"
# reverse_string = ""
# for i in range (len(name) -1, -1, -1):
#     reverse_string = reverse_string +name[i]

# print(f"reverse name is {reverse_string}")


def reverse_string(name):
    reverse_string = ""
    for i in range (len(name)-1, -1, -1):
        reverse_string = reverse_string + name[i]

    print(f"your reverse name is {reverse_string}")
    



reverse_string("Gurung")