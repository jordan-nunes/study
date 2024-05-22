ages = [35,32,50,33,48,50,33,48,22,49,35,38,20,47,49,48,34,21,48,44,48,30,25,42,42,23,25,23,38,35]
incomes = [3739,2219,3554,3978,4014,3270,4792,3879,2981,2384,4826,2460,3680,4318,1872,1770,4640,3929,3295,1729,3965,4267,4007,1916,2987,2943,3852,4543,2055,1730]

income_sum = 0
for income in incomes:
    income_sum += income
income_avg = income_sum / len(incomes)

employee_lower_avg = 0
for i, income in enumerate(incomes):
    if ages[i] >= 25 and income < income_avg:
        employee_lower_avg += 1

print("Employees older than 25 that earn less than the averange:", employee_lower_avg)