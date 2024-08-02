rank_dict = {}
while True:
    costumer_name = input("Enter the name of the customer (or 'exit' to exit): ")
    if costumer_name == 'exit' or costumer_name == 'q':
        break
    
    while True:
        try:
            purchases = int(input("Enter the total purchases: "))
            break
        except:
            print("Invalid input. Please enter a number for purchases.")

    if purchases < 1000:
        rank = 'Bronze'
    elif purchases >= 1000 and purchases < 5000:
        rank = 'Silver'
    else:
        rank = 'Gold'
    rank_dict.update({costumer_name : rank})

for costumer in rank_dict.keys():
    print("{}: Customer Segment = {}".format(costumer, rank_dict[costumer]))