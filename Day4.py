movies =[("title", "director", "release_year", "budget")]
movie2= (input("name of the movie: "), 
    input("name of the director: "),
    input("year of release: "), 
    input("movie budget: "))
print(f"Movie: {movie2[0]}, release year: {movie2[2]}")
movies.append(movie2)
print(movies)
movies.pop(0)
print(movies)