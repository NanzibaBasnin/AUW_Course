name = input("What's your name? ")


with open("names3.txt", "a") as file:
   file.write(f"{name}\n")

#automating the process does not require file close to save the file 



