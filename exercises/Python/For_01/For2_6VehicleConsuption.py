vehicles = ['fusca','gol', 'uno', 'vectra', 'peugeot']
consuptions = [7, 10, 12.5, 9, 14.5]

for i, vehicle in enumerate(vehicles):
    print("Car #", i)
    print("Name:", vehicles[i])
    print("Km / l:", consuptions[i])

#   For a 1000km ride with a $ 2.25 / liter
liter_consuptions = []
car_consuption = 0
for i, consuption in enumerate(consuptions):
    liter_consuption = 1000 / consuption
    liter_consuptions.append(liter_consuption)

    if consuption > car_consuption:
        most_economic_car = vehicles[i]

costs = []
for liter_consuption in liter_consuptions:
    cost = liter_consuption * 2.25
    costs.append(cost)

print("\nFinal output")
for i, vehicle in enumerate(vehicles):
    print("| {0} - {1}           -    {2} -  {3} l - R$ {4}".format(i, vehicle, consuptions[i], liter_consuptions[i], costs[i]))

print("Most economic is", most_economic_car)