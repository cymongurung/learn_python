fruits = []

total_no_fruits = int(input("enter total number of fruits: "))

for i in range(1,total_no_fruits+1):
    fruit = input(f"enter to to do {i}: ")
    fruits.append(fruit)

print("\n-------\n")
print("All fruits are are")

#Didplay all result


for fruit in fruits:
    print(fruit)
