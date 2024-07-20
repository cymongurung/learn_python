#create program that ask user to enter n no of todo and diplay it

todos = []

total_to_do = int(input("enter total number of todo: "))

for i in range(1,total_to_do+1):
    todo = input(f"enter to to do {i}: ")
    todos.append(todo)

print("\n-------\n")
print("All to to list are")

#Didplay all result


for todo in todos:
    print(todo)







