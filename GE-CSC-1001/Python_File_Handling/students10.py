import csv

students = []

with open("students1.csv") as file: 
    reader = csv.DictReader(file) #returns dictionary one at a time 
    for row in reader:
        students.append({"name":row["name"], "home": row["home"]})
        
#show an example where you flip the headers and still the program works 
#even if I add more columns the existing code will not break 
    


for student in sorted(students, key=lambda student: student["name"]): #impossible to sort dictionary 
    print(f"{student['name']} is in {student['home']}")
     

    