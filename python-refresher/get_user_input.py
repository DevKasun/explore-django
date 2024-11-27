monthly_income = float(input("Enter your monthly income: "))
monthly_savings = float(input("Enter your monthly savings: "))

monthly_saving_rate = (monthly_savings / monthly_income) * 100

print(f"Your monthly saving rate is: {monthly_saving_rate:.2f}%")
