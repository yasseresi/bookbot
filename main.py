abc = 'abcdefghijklmnopkrstuvwxyz'
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dic = create_dic()
    new_dic = parcour_text(text,dic)

    # printing the report 
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    sorted_list = to_list(dic,[*abc])
    for i in range(0,len(sorted_list)):
        print(f"The '{sorted_list[i]['caracter']}' caracter was found {sorted_list[i]['count']} times")
    print("--- End report ---") 
  


def to_list(dictionary,list_caracters):
    list = []
    for caracter in  list_caracters :
        list.append({"caracter": caracter , "count" : dictionary[caracter]})
    return sorted(list, reverse=True, key=sort_on)



def sort_on(dict):
    return dict["count"]


def create_dic() :
    dic = {}
    list_abc = [*abc]
    for c in list_abc :
        dic.update( {c : 0})
    return dic


def parcour_text(text,dic) : 
    words = text.lower().split()
    for word in words :
        caracters = [*word]
        for i in range(0,len(caracters)):
            if caracters[i] in dic:
                dic[caracters[i]] += 1 
    return dic
                      

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()