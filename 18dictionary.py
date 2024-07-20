expenses = {
'sunday' : 30,
'monday' : 43,
'tuesday' : 25,
'wednesday' : 44,
'thursday' : 23,
'friday' : 22,
'saturday' : 66,
}

# print(type(expenses))

total = sum(expenses.values())
print(f"total expenses is {total}")
print(f"average expense is {total/7} ") 