
# Create a function that accepts any number of numbers
# as positional arguments and prints the sum of those numbers


def sum_numbers(*numbers):
    return sum(numbers)

# Create a function that accepts any number of positional
# and keyword arguments, and that prints them back to the user.


def print_input(*positional, **keyword):
    positional = [repr(arg) for arg in positional]
    keyword = [f"{key} = {repr(value)}" for key, value in keyword.items()]
    print(f"Positional arguments are: {', '.join(positional)}")
    print(f"Keyword arguments are: {', '.join(keyword)}")


print_input(1,  "blue",  [1,  23,  3], height=184, key=lambda x: x ** 2)

# Print the following dictionary using the format
# method and ** unpacking.

country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

country_template = """
"Name": {name},
"Population": {population},
"Capital": {capital},
"Currency": {currency}
"""

print(country_template.format(**country))

# Using * unpacking and range, print the numbers
# 1 to 20, separated by commas.
print(*range(1, 21), sep=", ")


