from itertools import cycle

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

# Use the map function to find the sum of the numbers in each tuple.
# Use manual iteration to print the first two results
# provided by the resulting map object.

soma = map(lambda n: sum(n), numbers)
print(f"First result is: {next(soma)}")
print(f"Second result is: {next(soma)}")


# Imagine you have 3 employees and it's been agreed that the employees will
#  take it in turns to lock up the shop at night. Write a program to create
#  a schedule that lists which of your employees will lock up the shop
# on a given day over a 30 day period.

employees = cycle(["Amanda", "Felipe", "Iasmym"])
days = cycle(["Monday", "Tuesday", "Wednesday",
              "Thursday", "Friday", "Saturday", "Sunday"])

for day in range(1, 31):
    print(f"Day {day} ({next(days)}): {next(employees)} closes the store.")
