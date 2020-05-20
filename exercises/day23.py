# Write a generator that generates prime numbers in a specified range.
def prime_range(n, m):
    for number in range(n, m+1):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number


n = int(input("Please enter your start number: "))
m = int(input("Please enter your ending number: "))
prime = prime_range(n, m)
print(f"The prime numbers between {n} and {m} are:")
print(*prime, sep="\n")

# Rewrite this code using a generator expression
# map(lambda name: name.strip().title(), names)
names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
names = (name.strip().title() for name in names)
print(*names, sep=", ")


