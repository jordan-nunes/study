sales_dict = {}
while True:
    seller = input("Type the salesperson's name (or 'exit' to exit): ")
    if seller == 'exit' or seller == 'q':
        break
    
    while True:
        try:
            sale = int(input("Type the sales: "))
            break
        except:
            print("Invalid input. Please enter a number for sales.")
        
    if seller in sales_dict.keys():
        sales, quantity = sales_dict[seller]
        sales += sale
        quantity += 1
        sales_dict.update({seller : [sales, quantity]})
    else:
        quantity = 1
        sales_dict.update({seller : [sale, quantity]})

for key in sales_dict:
    sales, quantity = sales_dict[key]
    avg_sales = sales / quantity
    print("{}: Total sales = $ {}, Average sales = $ {}".format(key, sales, avg_sales))