numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]

movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}
movie={key.title(): name.title() for key, name in movie.items()}
print(movie)