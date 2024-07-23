## Ask user to enter todos and print all todo


total_todo = int(input("enter total todo"))

todos = []


for i in range(0, total_todo):
    todo = input(f"enter todo {i + 1}:")
                     

    todos.append(todo)

for todo in todos: 
    print(todo)