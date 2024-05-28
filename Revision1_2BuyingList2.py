def add_item(buying_dict):
    item = input("Write the product name to add: ")
    quantity = int(input("Write the quantity: "))
    buying_dict.update({item : quantity})
    return buying_dict

def remove_item(buying_dict):
    item = input("Write the product name to remove ")
    del buying_dict[item]
    return buying_dict

def see_list(buying_dict):
    print("Buying List:\n")
    for key in buying_dict:
        print("Product: {} - Quantity: {}".format(key, buying_dict[key]))
    return

print("Welcome to Your Buying List")
buying_dict = {}
while True:
    option = input("\n1 Add item\n2 Remove item\n3 See List\n4 Exit\nChoose an option: ")
    if option == '1':
        add_item(buying_dict)
    elif option == '2':
        remove_item(buying_dict)
    elif option == '3':
        see_list(buying_dict)
    elif option == '4':
        break
    else:
        print("**!Please, choose a valid option!**")