students = []

with open("students.csv") as file: 
    for line in file: 
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}       
        students.append(student)




for student in sorted(students): #impossible to sort dictionary 
    print(f"{student['name']} is in {student['house']}")
    

    