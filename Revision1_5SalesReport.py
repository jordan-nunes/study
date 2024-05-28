sales_dict = {}
while True:
    seller = input("Type the salesperson's name (or 'exit' to exit): ")
    if seller == 'exit' or seller == 'q':
        break
    
    while True:
        try:
            if seller in sales_dict.keys():
                sale = int(input("Type the sales: "))
                list_sales = sales_dict[seller]
                list_sales.append(sale)
                sales_dict.update({seller : list_sales})
                break
            else:
                sale = [int(input("Type the sales: "))]
                sales_dict.update({seller : sale})
                break
        except:
            print("Invalid input. Please enter a number for sales.")

for key in sales_dict:
    sum_sales_list = sum(sales_dict[key])
    avg_sales = sum_sales_list / len(sales_dict[key])
    print("{}: Total sales = $ {}, Average sales = $ {}".format(key, sum_sales_list, avg_sales))