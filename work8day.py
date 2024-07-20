months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

month_number = input("Enter a number (1-12) for the month: ")

if month_number.isdigit():
    month_number = int(month_number)
    if 1 <= month_number <= 12:
        print(f"The month is {months[month_number - 1]}.")
    else:
        print("Invalid number. Please enter a number between 1 and 12.")
else:
    print("Invalid input. Please enter a valid number.")
