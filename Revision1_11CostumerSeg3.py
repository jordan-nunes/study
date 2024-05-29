def request_customer_name():
    costumer_name = input("Enter the name of the customer (or 'exit' to exit): ")
    return costumer_name


def request_total_purchases():
    while True:
        try:
            purchases = int(input("Enter the total purchases: "))
            break
        except:
            print("Invalid input. Please enter a number for purchases.")
    return purchases


def assign_segment(*args):
    if purchases < 1000:
        rank = 'Bronze'
    elif purchases >= 1000 and purchases < 5000:
        rank = 'Silver'
    else:
        rank = 'Gold'
    rank_dict.update({costumer_name : rank})
    return rank_dict

def print_segment_by_customer(rank_dict):
    for costumer in rank_dict.keys():
        print("{}: Customer Segment = {}".format(costumer, rank_dict[costumer]))
    return

rank_dict = {}
while True:
    costumer_name = request_customer_name()
    if costumer_name == 'exit' or costumer_name == 'q':
        break
    
    purchases = request_total_purchases()

    assign_segment(rank_dict, purchases)

print_segment_by_customer(rank_dict)