
def add(x, y):
    return(x+y)

def subtract(x, y):
    return(x-y)

def divide(x, y):
    if y != 0:
        return(x/y)

def multiply(x, y):
    return(x*y)

def print_show_info(tv_show):
    for serie in tv_show:
        title = serie["title"]
        year = serie ["initial_release"]
        seasons = serie["seasons"]
        print(f"{title} ({year}) - {seasons} seasons")


series = [
 	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
 	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
 	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
 	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
 	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
 	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]
print_show_info(series)

def is_it_palindrome(word):
    word = word.strip().lower()
    reverse = word[::-1]
    if word == reverse:
        return("It's a palindrome!")

print(is_it_palindrome("Hannah"))

