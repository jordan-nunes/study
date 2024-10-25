def calculate_tax_rate(price, cost, profit):
    tax = price - cost - profit
    return tax / price

price = 1500
cost = 400
profit = 800

print(calculate_tax_rate(price, cost, profit))