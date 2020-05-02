dic= {
 	"album_name": "The Dark Side of the Moon",
 	"band": "Pink Floyd",
 	"year": 1973,
 	"songs": (
 		"Speak to Me",
 		"Breathe",
 		"On the Run",
 		"Time",
 		"The Great Gig in the Sky",
 		"Money",
 		"Us and Them",
 		"Any Colour You Like",
 		"Brain Damage",
 		"Eclipse"
 	)
 }


for key, value in dic.items():
    print(f"{key}: {value}")

del dic["songs"]
del dic["year"]

dic["release_date"] = "March 1st, 1973"