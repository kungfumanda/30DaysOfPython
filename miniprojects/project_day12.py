# reading list
# program that can store and display books from a user's reading list


def add_book(lis, book):
    lis.append(book)


def show_books(lis):
    for book in lis:
        title, author, year = book.values()
        print(f"{title}, by {author} ({year})")


reading_list = []
while True:
    action = input("""
Please enter one of the following options:
    
    [1] Add book 
    [2] See reading list 
    [-1] Exit

What would you like to do? """).strip()
    if action == "1":
        book = {
            "title": input("Enter the book's name: ").strip().title(),
            "author": input("Enter the author's name: ").strip().title(),
            "year": input("Enter the year of publication: ").strip()
        }
        add_book(reading_list, book)
        print("Book added! (:")
    elif action == "2":
        if reading_list:
            show_books(reading_list)
        else:
            print("Sorry, your reading list is empty.")
    elif action == "-1":
        break
    else:
        print("Sorry, this isn't a valid option.")
