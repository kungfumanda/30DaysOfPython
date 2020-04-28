#weekly earnings calculator

name = input("Enter employee's name: ").strip().title()
hourly_wage = float(input(f"Enter {name}'s hourly wage: "))
hours_worked = float(input(f"Enter hours worked by {name} this week: "))

week_earnings = hourly_wage * hours_worked

print("{} earned ${:.2f} this week".format(name, week_earnings))