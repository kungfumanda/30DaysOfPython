# sets
south_america = set()
south_america.update(["Brazil", "Chile", "Mexico"])
biggest_countries = {"Russia", "Canada", "Brazil"}

union_countries = south_america.union(biggest_countries)
symdif_countries = south_america.symmetric_difference(biggest_countries)
inters_countries = south_america.intersection(biggest_countries)

print(union_countries)
print(symdif_countries)
print(inters_countries)

sequence = range(8,42)
if int(input("Please enter a number: ")) in sequence:
    print("Your number is within the range")
