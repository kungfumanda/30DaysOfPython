employees = [
    #(name, hours worked, hourly rate)
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
average = 0
for i in range(len(employees)):
    print(f"{employees[i][0]}'s weekly payment should be ${employees[i][1] * employees[i][2]:.2f}")
    average += employees[i][2]

average = average/len(employees)
for i in range(len(employees)):
    if employees[i][2] > average:
        print(f"{employees[i][0]} is earning above average.")