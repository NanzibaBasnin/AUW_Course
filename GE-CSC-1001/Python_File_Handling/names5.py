name = input("What's your name? ")

#lets save the name for a person in a file, but to do that we need to 'open' a file
#open includes the name of the file we want to open, and optionally how we want to open it. 

file = open("names1.txt", "a")
 #a means append

file.write(name)
file.close()



