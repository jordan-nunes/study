def best_sellers(target, sales_lib):
    best_sellers = []
    for seller, sale in sales_lib.items():
        if sale >= target:
            best_sellers.append(seller)
    avg_best_sellers = len(best_sellers) / len(sales_lib)
    return best_sellers, avg_best_sellers

target = 10000
sales = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

print(best_sellers(target, sales))