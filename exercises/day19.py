# Create a short program that prompts the user for a list of grades 
# separated by commas. Split the string into individual grades and 
# use a list comprehension to convert each string to an integer. 
# You should use a try statement to inform the user when the values 
# they entered cannot be converted.

grades = input("Please enter your grades, separated by commas: ")
try:
    grades = grades.split(",")
    grades = [int(grade) for grade in grades]
except ValueError:
    print("Your values cannot be converted.")


# Imagine you have a file named data.txt. Open it for reading using Python, 
# but make sure to use a try block to catch an exception that arises if 
# the file doesn't exist. 

try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("There's no such file.")
 
