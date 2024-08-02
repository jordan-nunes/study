def request_salesperson_name():
    seller = input("Type the salesperson's name (or 'exit' to exit): ")
    return seller

def request_sales():
    while True:
        try:
            sale = int(input("Type the sales: "))
            break
        except:
            print("Invalid input. Please enter a number for sales.")
    return sale

def update_data(*args):
    if seller in sales_dict.keys():
        sales, quantity = sales_dict[seller]
        sales += sale
        quantity += 1
        sales_dict.update({seller : [sales, quantity]})
    else:
        quantity = 1
        sales_dict.update({seller : [sale, quantity]})
    return sales_dict

def print_data():
    for key in sales_dict:
        sales, quantity = sales_dict[key]
        avg_sales = sales / quantity
        print("{}: Total sales = $ {}, Average sales = $ {}".format(key, sales, avg_sales))

sales_dict = {}
while True:
    seller = request_salesperson_name()
    if seller == 'exit' or seller == 'q':
        break

    sale = request_sales()
    
    sales_dict = update_data(seller, sale, sales_dict)

print_data()