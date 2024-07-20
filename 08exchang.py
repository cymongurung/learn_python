container1 = "Milk"
container2 = "water"
#you can change from here
#you can change till here

# print(f"container 1 contains {container1}")
# print(f"container 2 contains {container2}")

# print(f"container 1 contains {container2}")
# print(f"container 2 contains {container1}")

container1, container2 = container2, container1

print(f"container 1 contains {container1}")
print(f"container 2 contains {container2}")
