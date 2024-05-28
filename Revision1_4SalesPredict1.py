data_dict = {}
validation = False
while True:
    product_name = input("Type the product name (or 'exit' to exit): ")
    if product_name == 'exit' or product_name == 'q' or product_name == 'quit':
            break
    while True:
        try:
            month_sales = int(input("Type the current month's sales: "))            
            break
        except:
            print("Invalid input. Please enter a number for growth rate.")
    while True:
        try:
            growth_rate = int(input("Type the growth rate (%): ")) / 100
            break
        except:
            print("Invalid input. Please enter a number for growth rate.")
    data_dict.update({product_name : (month_sales, growth_rate)})

for product in data_dict.keys():
    month_sale, growth = data_dict[product]
    forecast = month_sale + (month_sale * growth)
    print("{}: Next month's sales forecast = $ {}".format(product, forecast))