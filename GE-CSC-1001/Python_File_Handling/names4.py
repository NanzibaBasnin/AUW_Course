name = input("What's your name? ")

#lets save the name for a person in a file, but to do that we need to 'open' a file
#open includes the name of the file we want to open, and optionally how we want to open it. 

file = open("names.txt", "w")
 #w will help me open the file in a way to allow me change the contents 
file.write(name)
file.close()



