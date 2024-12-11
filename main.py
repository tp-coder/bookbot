def menu():
    print("What you would you like to do?")
    print("Choose 1 to read the book, 2 to know how many words the book has, and 3 to count the characters.")
    option = input("Enter your choice: 1, 2 or 3? ")
    print("Got it!")
    
    if option == "1":
        read_book()
        exit()
    elif option == "2":
        count_words()
        exit()
    elif option == "3":
        count_characters()
        exit()
    else:
        print("Invalid choice. Please try again.")

def read_book():
    try:
        with open("./books/Frankenstein.txt") as f:
            read_book = f.read()
            print(read_book)

    except FileNotFoundError:
        print("Path to the book not found.")

def count_words():
    try:
        with open("./books/Frankenstein.txt") as f:
            count_words = len(f.read().split())
            print(f"The book has {count_words} words")

    except FileNotFoundError:
        print("Path to the book not found.")

def count_characters():
    try:
        with open("./books/Frankenstein.txt") as f:
            book = f.read().strip()
            count_characters = 0

            for letter in book:
                count_characters += 1

            print(count_characters)                

    except FileExistsError:
        print("Path to the book not found.")

def main():
    while True:
        menu()

if __name__ == "__main__":
    main()