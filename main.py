from stats import *
import sys


def main():
    #sys.args[0] = "python3 main.py"
    #sys.args[1] = "./books/frankenstein.txt"
    #print(len(sys.argv))
    if len(sys.argv) <= 1:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
        
        
    

    the_book = get_book_text( sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print("Found", word_count(the_book) , "total words")
    #print(character_count(the_book))
    print("--------- Character Count -------")
    #print(sort_list(the_book))
    for item in sort_list(the_book):
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()