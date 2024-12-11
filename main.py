def menu():
    print("What you would you like to do?")
    print("Choose 'Read' to read the book and 'count' to know how many words the book has.")
    option = input("Enter your choice: read or count? ").strip().lower()
    print("Got it!")
    
    if option == "read":
        read_the_book()
        exit()
    elif option == "count":
        count_the_words()
        exit()
    else:
        print("Invalid choice. Please try again.")

def count_the_words():
    try:
        with open("./books/Frankenstein.txt") as f:
            file_contents = f.read()
            word_count = len(file_contents.split())
            print(f"The book has {word_count} words")
    except FileNotFoundError:
        print("Path to the book not found.")

def read_the_book():
    try:
        with open("./books/Frankenstein.txt") as f:
            file_contents = f.read()
            print(file_contents)
    except FileNotFoundError:
        print("Path to the book not found.")

def main():
    while True:
        menu()

if __name__ == "__main__":
    main()