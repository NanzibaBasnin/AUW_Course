import matplotlib.pyplot as plt
import csv

young = 0
middle = 0
old = 0

with open("cheat.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        age = int(row["Age"])
        cheated = row["Cheated"]

        if cheated == "true":

            if age <= 25:
                young += 1

            elif age <= 45:
                middle += 1

            else:
                old += 1


groups = ["Young", "Middle Age", "Old"]
values = [young, middle, old]

plt.bar(groups, values)

plt.xlabel("Age Group")
plt.ylabel("Number of People Who Cheated")
plt.title("Cheating Behavior by Age Group")

plt.grid(axis="y")
plt.show()