from operator import methodcaller

# Use map to call the strip method on each string in the following list
# and print the lines of the nursery rhyme on different lines in the console.
humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",
    "    Couldn't put Humpty together again."
]
humpty_dumpty = map(methodcaller("strip"), humpty_dumpty)
print(*humpty_dumpty, sep="\n")


# Below you'll find a tuple containing several names.Use a list comprehension with
# a filtering condition so that only names with fewer than 8 characters
# end up in the new list. Make sure that every name
#  in the new list is in title case.
names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
names = map(methodcaller("title"), filter(lambda name: len(name) < 8, names))
print(*names, sep=", ")

# Use filter to remove all negative numbers from the following range: range(-5, 11).
# Print the remaining numbers to the console
numbers=filter(lambda number: number >= 0, range(-5, 11))
print(*numbers)
