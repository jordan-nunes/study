products = []

while True:
    data = []
    name = input("Type a product name: ")
    if name != '':
        data.append(name)
        pass
    else:
        break

    quantity = input("Type the product quantity: ")
    if quantity != '':
        data.append(quantity)
        pass
    else:
        break
    products.append(data)

for product in products:
    print("Product: {0} - Quantity: {1}".format(product[0], product[1]))