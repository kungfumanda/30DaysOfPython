#movie budgets
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
if int(input("Do you wanna add more movies? [0] no [1] yes: ")):
    for i in range(int(input("How many movies? "))):
        name = input(f"Whats the {i+1}th movie's name? ")
        budget = int(input("Whats its budget? "))
        movies.append((name, budget))

average = 0
for movie in movies:
    average += movie[1]
average = average / len(movies)

count = 0
for movie in movies:
    if movie[1] > average:
        print(f"{movie[0]}'s budget was ${movie[1]:,}, and so ${movie[1]-average:,} above average.")
        count += 1
print(f"{count} movies's budgets were above average.")