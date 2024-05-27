print("Welcome to Your Buying List")
buying_dict = {}
while True:
    option = input("\n1 Add item\n2 Remove item\n3 See List\n4 Exit\nChoose an option: ")
    if option == '1':
        item = input("Write the product name to add: ")
        quantity = int(input("Write the quantity: "))
        buying_dict.update({item : quantity})
    elif option == '2':
        item = input("Write the product name to remove ")
        del buying_dict[item]
    elif option == '3':
        print("Buying List:\n")
        for key in buying_dict:
            print("Product: {} - Quantity: {}".format(key, buying_dict[key]))
    elif option == '4':
        break
    else:
        print("**!Please, choose a valid option!**")