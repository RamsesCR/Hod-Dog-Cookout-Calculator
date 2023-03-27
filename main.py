import math

numPersons = int(input("Enter the number of guests expected to attend the cookout: "))

numHotdogPersons = int(input("Enter the amount of hot dogs that will be provided to each person: "))

bunsPerPackage = 8

totalHotdogs = numHotdogPersons * numPersons

hotdogPackage = math.ceil(totalHotdogs / 10)

bunsNeeded = totalHotdogs // bunsPerPackage

if totalHotdogs % bunsPerPackage != 0:
    bunsNeeded += 1

hotdogsLeftover = (hotdogPackage * 10) - totalHotdogs

bunsLeftover = (bunsNeeded * bunsPerPackage) - totalHotdogs

print("Minimum number of hot dog packages required:", hotdogPackage)
print("Minimum number of hot dog buns required:", bunsNeeded)
print("Number of hot dogs left over:", hotdogsLeftover)
print("Number of hot dog buns left over:", bunsLeftover)