from stats import text2words
from stats import count_chars
from stats import sort_list
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    output1 = text2words(book_text)
    print(f"{output1} words found in the document")
    output2 = count_chars(book_text)
    output3 = sort_list(output2)

    print("==================BookBOT==================")
    print(f"Analyzing book found at {file_path}")
    print("----------------- Word Count----------------")
    print(f"Found {output1} total words")
    print("---------------- Character Count ------------")
    for char_dict in output3:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("==================== END ====================")
main()
    
