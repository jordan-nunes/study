print("Welcome to Your Buying List")
buying_list = []
while True:
    option = int(input("\n1 Add item\n2 Remove item\n3 See List\n4 Exit\nChoose an option: "))
    if option == '1':
        item = input("Write the product name to add: ")
        buying_list.append(item)
    elif option == '2':
        item = input("Write the product name to remove ")
        while item not in buying_list:
            item = input("Invalid product, try again ")
        buying_list.remove(item)
    elif option == '3':
        print("Buying List:\n", '\n'.join(buying_list))
    elif option == '4':
        break
    else:
        print("**!Please, choose a valid option!**")