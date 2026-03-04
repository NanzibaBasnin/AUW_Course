#lets print plus sort them alphabetically


names = []

for _ in range(3):
    name = input("Whats your name?")
    names.append(name)


for name in sorted(names):
    print(f"hello, {name}")

#if i run this program again, all information will be lost, that is where File i/o comes in.. 

