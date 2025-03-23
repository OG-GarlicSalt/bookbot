def text2words(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def count_chars(book_text):
    lower_case = book_text.lower()
    output_dic = {}
    for l in lower_case:
            if l in output_dic:
                output_dic[l] += 1
            else:
                output_dic[l] = 1
    return output_dic

def sort_list(dict):
     char_list = []
     for char, count in dict.items():
          char_list.append({"char": char, "count": count})
     char_list.sort(reverse=True, key=lambda dict_item: dict_item["count"])
     return char_list