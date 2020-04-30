complete_name = input("Please enter your name and last name: ")
first_name = complete_name.split()[0]
surname = complete_name.split()[1]

#------------------------------------#

n = [str(i) for i in range(1,6)]
a = " | ".join(n)
print(a)

#---------------------------------#
quotes = [
 	"'What a waste my life would be without all the beautiful mistakes I've made.'",
 	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
 	"'The very essence of romance is uncertainty.'",
 	"'We are not here to do what has already been done.'"
]
for quote in quotes:
     print(quote[1:-1].strip())

#---------------------------------------#

word = input("please enter a word").strip()
print(f"your word has {len(word)} letters.")

