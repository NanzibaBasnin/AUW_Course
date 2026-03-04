#iterate the file plus print it in a sorted order 


names =[]

with open("names3.txt") as file: 
    for line in file:
        names.append(line.rstrip())


for name in sorted(names):
    print(f"hello, {name}")

