students = []

with open("students.csv") as file: 
    for line in file: 
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}       
        students.append(student)


def get_house(student):
    return student["house"]

#python allows to pass functions as parameters 

for student in sorted(students, key=get_house): #impossible to sort dictionary 
    print(f"{student['name']} is in {student['house']}")
    

    