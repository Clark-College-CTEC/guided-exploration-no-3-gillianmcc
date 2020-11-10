# Guided Exploration No. 3
# Gillian McCarthy

# import the python random library
import random

# create an empty list to store rap names
possible_names = []

# open a new file to store generated names
outputFile = open('rap-names-output.txt', 'w')

# open file for read access
with open("rap-names.txt", "r") as dataFile:
    # assign a handle to the file
    for name in dataFile:
        # append a new name to the file
        possible_names.append(name.rstrip())

# ask user how many names they want to generate and assign that
# number to var 'count'
count = int(input('How many rap names would you like to create? '))
# ask user how many parts they want in their name and
# assign that num to var 'parts'
parts = int(input('How many parts should the name contain? '))

# create a counted loop using 'count' var
for i in range(count):
    # create an empty list to hold rap name parts
    name_parts = []
    # create another counted loop using var 'parts'
    for j in range(parts):
        # add the num of 'parts' user wants to 'name_parts' list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
    # write the new name into the file
    outputFile.write(f"{' '.join(name_parts)}\n")
    # print the new name
    print(f"{' '.join(name_parts)}")

# close the file
outputFile.close()
