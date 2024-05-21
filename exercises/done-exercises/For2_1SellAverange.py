sales = [1000, 1500, 1200, 1300]
sellers = ["Fulano", "Beltrano", "Ciclano", "Lira"]

sum = 0
for sale in sales:
    sum += sale
averange = sum / len(sales)

print("Averange sales:", averange)

for i, seller in enumerate(sellers):
    print(sellers[i], "sold:", sales[i])