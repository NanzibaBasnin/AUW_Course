#write code that reads the names on the file 

with open("names3.txt", "r") as file: 
    for line in file:
        print("hello,",line.rstrip())