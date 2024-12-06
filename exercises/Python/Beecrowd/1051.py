salary = float(input())
tax1 = 8
tax2 = 18
tax3 = 28

if salary >= 2000.01 and salary <= 3000:   
    salary_tax = (salary- 2000)*(tax1 / 100)
    print("R$ {:.2f}".format(salary_tax))

elif salary >= 3000.1 and salary <= 4500:
    salary_tax = 1000 * (tax1 / 100) + (salary - 3000)*(tax2 / 100)
    print("R$ {:.2f}".format(salary_tax))

elif salary > 4500:
    salary_tax = 1000 * (tax1 / 100) + 1500 * (tax2 / 100) + (salary - 4500)*(tax3 / 100)
    print("R$ {:.2f}".format(salary_tax))
else:
    print("Isento")
