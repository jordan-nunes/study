data_dict = {}
while True:
    product_name = input("Type the product name (or 'exit' to exit): ")
    if product_name == 'exit' or product_name == 'q' or product_name == 'quit':
            break
    month_sales = int(input("Type the current month's sales: "))
    growth_rate = int(input("Type the growth rate (%): ")) / 100
    data_dict.update({product_name : (month_sales, growth_rate)})

for product in data_dict.keys():
    month_sale, growth = data_dict[product]
    forecast = month_sale + (month_sale * growth)
    print("{}: Next month's sales forecast = $ {}".format(product, forecast))