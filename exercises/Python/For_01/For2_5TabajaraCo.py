salary_list = [1000, 300, 500, 200, 1500, 3000, 3400, 5000, 7000, 2000, 600, 800, 250, 1500, 20000]
bonuses = []

print("Projection of Allowance Spending\n")

bonus_amount = 0
minimun_bonus = 0
for salary in salary_list:
    print("Salary:", salary)

    bonus = salary * 0.20
    if (salary * 0.20) <= 100:
        bonus = 100
        bonuses.append(bonus)
        minimun_bonus += 1
    else:
        bonuses.append(bonus)
    
    bonus_amount += bonus

print("\nSalary - Bonus")

greater_bonus = 0
for i, bonus in enumerate(bonuses):    
    print("$", salary_list[i], "- $", bonus)
    
    if greater_bonus < bonus:
        greater_bonus = bonus

earned_bonus = len(bonuses)
print("\nTotal employees that earned bonus:", earned_bonus, "employees")
print("Total bonuses given: $", bonus_amount)
print("Minimum bonus given to", minimun_bonus)
print("Greater bonus value: $", greater_bonus)