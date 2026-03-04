with open("students.csv") as file: 
    for line in file: 
        name, house = line.rstrip().split(",") #creating 2 variables at once 
        print(f"{name} is in {house}")  
        