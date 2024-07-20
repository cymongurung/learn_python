n1 = 100
n2 = 200
n3 = 300

if n1 > n2 and n1 > n3:
    print(f"{n1} is a great number.")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is a great number.")
elif n3 > n1 and n3 > n2:
    print(f"{n3} is a great number.")
else:
    print("Something went wrong")
