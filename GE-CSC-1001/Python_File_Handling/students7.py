students = []

with open("students1.csv") as file: 
    for line in file: 
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}       
        students.append(student)




#python allows to pass functions as parameters 

#lambda anonymous function 


for student in sorted(students, key=lambda student: student["name"]): #impossible to sort dictionary 
    print(f"{student['name']} is in {student['home']}")
    

    