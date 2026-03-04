#write code that reads the names on the file 

with open("names3.txt", "r") as file: 
    lines = file.readlines()
    #reading all the files storing it in a variable called lines 

for line in lines: 
    print("hello, ", line.rstrip())
