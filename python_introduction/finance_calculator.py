use = input("Enter your monthly income: ")
monthly_income = int(user)
user2 = input("Enter your total monthly expenses: ")
monthly_expenses = int(user2)
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings}")
annual_interest_rate = 0.15
Projected_year_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)
print(f"projected savings after one year, with interest, is: {Projected_year_savings}")
