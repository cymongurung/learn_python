names = [
#name , age , department
 ("Sagar Aryal", "Microbiology"),
    ("Santosh Adhikari", "IT"),
    ("Subin Thapa", "IT"),
    ("Mandip Hirachan", "IT"),
    ("Sujan Khadka", "Finance"),
    ("Samayak Pokharel", "MBA"),
    ("Binod Rayamajhi", "Microbiology")


]

##find all from Microbioloy department

# microbiology_names = [name[0] for name in names if name[1] == "Microbiology"]

# print(microbiology_names)


it_names = [name[0] for name in names if name[1] == "IT"]

print(it_names)