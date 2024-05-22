goal = 10000
sales = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

best_seller = []

#Gets the sellers that have reach the goal
for seller in sales:
    if seller[1] >= goal:
        best_seller.append(seller)

print(best_seller)