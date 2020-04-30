# guessing game
n = 42
while True:
    guess = int(input("Tell me your next guess: "))
    if (n == guess):
        print("Congrats, you won!")
        break
    elif (n > guess):
        print("A little bit higher.")
    else:
        print("A little bit lower")

# prints out every letter in python except "o"
for letter in "python":
    if letter == "o":
        continue
    else:
        print(letter)

# prints out every prime number between 1 and 100
for number in range(2, 101):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(f"{number} is prime.")
