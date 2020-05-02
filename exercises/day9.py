main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]
#using destructuring
for character, actor, species in main_characters:
    print(f"{character} is a {species.lower()} voiced by {actor}.")

name, number_id, (major_discipline, minor_discipline) = ("John Smith", 11743, ("Computer Science", "Mathematics"))

