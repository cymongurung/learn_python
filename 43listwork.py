#creating list
names = ['Anish ', 'Binod', 'Ratna']
expenses = [1000, 2500, 410 ]



# in case we need to know the data type the names should be define with positon eg here[0]
# print(type(names[0]))
# print(type(expenses))



# to add the items in list.

# names.append("")


names.append('Mahesh Gautam')

names.append('prakash Gautam')
names.append('Suman Gurung')



names.pop()

total_manish = names.count('Mahesh Gautam')
print(total_manish)

for name in names:
    print(name)


print(names[1])

    # remove last item from list
# names.pop example 

# find total number of occurences.
#  eg names.count("suman gurung")

# index
# eg. print(names[1])


print(names.index('prakash Gautam'))