#reverse the file list 
names =[]
with open("C:\Users\HP\") as file: 
    for line in file:
         names.append(line.restrip())
        
for name in sorted(names, reverse =True):
     print(f"hello, {name}")



