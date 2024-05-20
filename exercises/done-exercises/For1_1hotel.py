num_people = int(input("How many people will be in the room? "))

guests_data = []

#Adds each guest data to list guests_data
for people in range(num_people):
    data = []
    name = input("Name, please: ")
    ssn = input("Social Security Number, please: ")
    data.append(name)
    data.append(ssn)
    guests_data.append(data)

print(guests_data)