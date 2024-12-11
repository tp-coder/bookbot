from collections import Counter
# Global path variable
path = "books/Frankenstein.txt"

def menu():
    print("What you would you like to do?")
    print("Choose 1 to read the book, 2 to know how many words the book has, 3 to count the characters, and 4 to print the book report.")
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
    elif option == "4":
        report()
        exit()
    else:
        print("Invalid choice. Please try again.")

def read_book():
    try:
        with open(path) as f:
            read_book = f.read()
            print(read_book)

    except FileNotFoundError:
        print("Path to the book not found.")

def count_words():
    try:
        with open(path) as f:
            count_words = len(f.read().split())
            print(f"{count_words} found in the document")

    except FileNotFoundError:
        print("Path to the book not found.")

def count_characters():
    try:
        with open(path) as f:
            book = f.read().lower()
            letters = [char for char in book if char.isalpha()]
            count_letters = Counter(letters)

            for char, count in sorted(count_letters.items()):
                print(f"The '{char}' character was found '{count}' times")           

    except FileNotFoundError:
        print("Path to the book not found.")

def report():
    try:
        print(f"--- Begin report of {path} ---")
        count_words()
        print()
        count_characters()

    except FileNotFoundError:
        print("Path to the book not found.")

def main():
    while True:
        menu()

if __name__ == "__main__":
    main()