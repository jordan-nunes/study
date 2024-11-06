goal = 10000
sales = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

best_sellers = []
for data in sales:
    name, sale = data
    if sale >= goal:
        best_sellers.append(data)

print("The Best Sellers are:\n")
for bests_data in best_sellers:
    name, sale = bests_data
    print(f"{name} sold: {sale}")