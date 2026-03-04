students = []

with open("students.csv") as file: 
    for line in file: 
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}       
        students.append(student)




#python allows to pass functions as parameters 

#lambda anonymous function 

for student in sorted(students, key=lambda student: student["name"]): #impossible to sort dictionary 
    print(f"{student['name']} is in {student['house']}")
    

    